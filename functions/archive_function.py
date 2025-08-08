import datetime
import json
from azure.cosmos import CosmosClient
from azure.storage.blob import BlobServiceClient

def archive_old_records():
    cutoff_date = datetime.datetime.utcnow() - datetime.timedelta(days=90)
    
    cosmos_client = CosmosClient("<COSMOS_ENDPOINT>", "<COSMOS_KEY>")
    container = cosmos_client.get_database_client("BillingDB").get_container_client("Records")

    blob_client = BlobServiceClient.from_connection_string("<BLOB_CONNECTION_STRING>")
    archive_container = blob_client.get_container_client("billing-archive")

    query = f"SELECT * FROM Records r WHERE r.timestamp < '{cutoff_date.isoformat()}'"
    for record in container.query_items(query, enable_cross_partition_query=True):
        blob_name = f"{record['id']}.json"
        archive_container.upload_blob(blob_name, json.dumps(record), overwrite=True)
        container.delete_item(record, partition_key=record['partitionKey'])
