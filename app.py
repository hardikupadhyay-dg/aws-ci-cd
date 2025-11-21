import json
from src.calculator import add, subtract, product

def lambda_handler(event, context):
    print("EVENT RECEIVED:", event)

    # Parse request body if it's from API Gateway
    if isinstance(event, dict) and "body" in event:
        try:
            event = json.loads(event["body"])
        except Exception:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid JSON body"}),
                "headers": {"Content-Type": "application/json"}
            }

    operation = event.get("operation")
    a = event.get("a")
    b = event.get("b")

    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "product":
        result = product(a, b)
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid operation"}),
            "headers": {"Content-Type": "application/json"}
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"result": result}),
        "headers": {"Content-Type": "application/json"}
    }
