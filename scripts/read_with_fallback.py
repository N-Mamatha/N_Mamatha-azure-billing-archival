# Billing record fetch logic with fallback (Python pseudocode)
def get_billing_record(record_id):
    record = cosmos.get(record_id)
    if record:
        return record
    else:
        return blob.download_json("archive", record_id + ".json")
