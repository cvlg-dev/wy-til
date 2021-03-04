def add(x, y):
    """
    Add Function
    """
    return x + y


def subtract(x, y):
    """
    Subtract Function
    """
    return x - y


def multiply(x, y):
    """
    Multiply Function
    """
    return x * y


def divide(x, y):
    """
    Divide Function
    """
    if y == 0:
        raise ZeroDivisionError("Can't perform division by zero")
    return x / y