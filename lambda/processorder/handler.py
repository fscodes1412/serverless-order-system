import json

def handler(event, context):
    for record in event["Records"]:
        order = json.loads(record["body"])
        print("Processing order:", order)

    return {"status": "processed"}
