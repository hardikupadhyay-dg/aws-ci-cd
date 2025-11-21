import json
from src.calculator import add, subtract, product

def lambda_handler(event, context):
    print("EVENT RECEIVED:", event)

    # If request comes from API Gateway, body will be a string
    if "body" in event:
        event = json.loads(event["body"])

    operation = event.get("operation")
    a = event.get("a")
    b = event.get("b")

    if operation == "add":
        return {"statusCode": 200, "body": json.dumps({"result": add(a, b)})}
    elif operation == "subtract":
        return {"statusCode": 200, "body": json.dumps({"result": subtract(a, b)})}
    elif operation == "product":
        return {"statusCode": 200, "body": json.dumps({"result": product(a, b)})}
    else:
        return {"statusCode": 400, "body": json.dumps({"error": "Invalid operation"})}
