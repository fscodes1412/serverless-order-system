import json
import boto3
import os

sqs = boto3.client('sqs')

QUEUE_URL = os.environ.get("QUEUE_URL")

def handler(event, context):
    body = json.loads(event["body"])

    order = {
        "order_id": body.get("order_id"),
        "item": body.get("item"),
        "quantity": body.get("quantity")
    }

    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(order)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Order sent to queue", "order": order})
    }
