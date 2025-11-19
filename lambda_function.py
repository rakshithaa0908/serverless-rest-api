import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("registration-form")

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "OPTIONS,POST"
}

def response(status, body):
    return {
        "statusCode": status,
        "headers": CORS_HEADERS,
        "body": json.dumps(body)
    }

def lambda_handler(event, context):

    if event.get("httpMethod") == "OPTIONS":
        return response(200, {})

    if event.get("httpMethod") != "POST":
        return response(405, {"message": "Only POST allowed"})

    try:
        body = event.get("body")
        if not body:
            return response(400, {"message": "No body received"})

        data = json.loads(body)

        required = ["first_name", "last_name", "address", "email", "phno"]
        for r in required:
            if r not in data:
                return response(400, {"message": f"Missing field: {r}"})

        table.put_item(Item={
            "email": data["email"].lower(),
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "address": data["address"],
            "phno": data["phno"]
        })

        return response(200, {"message": "Inserted"})

    except Exception as e:
        return response(500, {"message": "Server error", "error": str(e)})
