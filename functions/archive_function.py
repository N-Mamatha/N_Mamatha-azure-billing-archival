
# Archive Durable Function (Python pseudocode)
def archive_old_records():
    records = cosmos.query("SELECT * FROM Billing WHERE timestamp < NOW() - 90 days")
    for record in records:
        blob.upload_json(container="archive", name=record["id"] + ".json", data=record)
        cosmos.delete(record["id"])
