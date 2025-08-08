import json
from azure.cosmos import CosmosClient
from azure.storage.blob import BlobServiceClient

def get_billing_record(record_id, partition_key):
    cosmos_client = CosmosClient("<COSMOS_ENDPOINT>", "<COSMOS_KEY>")
    container = cosmos_client.get_database_client("BillingDB").get_container_client("Records")

    try:
        record = container.read_item(record_id, partition_key=partition_key)
        return record
    except:
        blob_client = BlobServiceClient.from_connection_string("<BLOB_CONNECTION_STRING>")
        archive_container = blob_client.get_container_client("billing-archive")
        blob = archive_container.download_blob(f"{record_id}.json")
        return json.loads(blob.readall())
