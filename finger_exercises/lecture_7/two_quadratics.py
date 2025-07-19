# two_quadratics.py
from eval_quadratic import eval_quadratic


def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    """
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    Evaluates one quadratic with coefficients a1, b1, c1, at x1.
    Evaluates another quadratic with coefficients a2, b2, c2, at x2.
    Prints the sum of the two evaluations. Does not return anything.
    """
    value1 = eval_quadratic(a1, b1, c1, x1)
    value2 = eval_quadratic(a2, b2, c2, x2)
    value = value1 + value2
    print(value)


if __name__ == "__main__":
    a1 = 1
    b1 = 1
    c1 = 1
    x1 = 1
    a2 = 1
    b2 = 1
    c2 = 1
    x2 = 1
    two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)
