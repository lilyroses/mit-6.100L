# apply.py


def apply(criteria, n):
    """
    * criteria: function that takes in a number and returns a bool
    * n: an int
    Returns how many ints from 0 to n (inclusive) match the criteria
    (i.e. return True when run with criteria) """
    count = 0
    for i in range(n+1):
        if criteria(i):
            count += 1
    return count


def is_even(x):
    return x % 2 == 0


def is_5(x):
    return x == 5


print(apply(is_even, 10))
print("apply with is_5:", apply(is_5, 10))
print("apply with lambda function:", apply(lambda x: x == 5, 100))

print(is_even(8))
print((lambda x: x % 2 == 0)(8))
