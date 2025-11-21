def add(a, b):
    if a < 0 or b < 0:
        raise ValueError("Only positive integers allowed")
    return a + b

def subtract(a, b):
    if a < 0 or b < 0:
        raise ValueError("Only positive integers allowed")
    if b > a:
        raise ValueError("Result would be negative")
    return a - b

def product(a, b):
    if a < 0 or b < 0:
        raise ValueError("Only positive integers allowed")
    return a * b
