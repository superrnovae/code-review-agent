def multiply(a, b):
    """Return the product of two numbers, with type checking."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Inputs must be numbers")
    return a * b
