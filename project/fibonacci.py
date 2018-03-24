def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

def fibonacci1(value):
    """
    Leveraging a Python generator and non-recursive
    """
    result = None
    fiber = fib()
    for iteration in xrange(0, value):
        result = fiber.next()
    return result

def fibonacci2(value):
    """
    This is a recursive implementation
    """
    if value == 0: return None
    elif value == 1: return 0
    elif value == 2: return 1
    return fibonacci2(value-1) + fibonacci2(value-2)
