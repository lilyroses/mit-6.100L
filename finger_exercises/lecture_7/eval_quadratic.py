# eval_quadratic.py

def eval_quadratic(a, b, c, x):
    """
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    Returns the value of the quadratic a×x² + b×x + c.
    """
    value = (a * (x**2)) + (b * x) + c
    return value


if __name__ == "__main__":
    a = 1
    b = 1
    c = 1
    x = 1
    print(eval_quadratic(a,b,c,x))