from src.calculator import add, subtract, product

def lambda_handler(event, context):
    operation = event.get("operation")
    a = event.get("a")
    b = event.get("b")

    if not isinstance(a, int) or not isinstance(b, int):
        return {"error": "a and b must be integers"}

    if operation == "add":
        return {"result": add(a, b)}
    elif operation == "subtract":
        return {"result": subtract(a, b)}
    elif operation == "product":
        return {"result": product(a, b)}
    else:
        return {"error": "unsupported operation"}
