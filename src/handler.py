import json
import os
import uuid
from datetime import datetime, timezone

import boto3

table = boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])

def response(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }

def handler(event, context):
    route = event.get("routeKey", "")

    if route == "POST /notes":
        try:
            data = json.loads(event.get("body") or "{}")
        except json.JSONDecodeError:
            return response(400, {"error": "Body must be valid JSON"})

        text = str(data.get("text", "")).strip()
        if not text:
            return response(400, {"error": "Field 'text' is required"})
        if len(text) > 500:
            return response(400, {"error": "Field 'text' must be 500 characters or fewer"})

        item = {
            "id": str(uuid.uuid4()),
            "text": text,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        table.put_item(Item=item)
        return response(201, item)

    if route == "GET /notes":
        result = table.scan(Limit=50)
        return response(200, result.get("Items", []))

    return response(404, {"error": "Not fount"})