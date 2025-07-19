def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    n = len(tA)
    pairwise_products = []
    
    for i in range(n):
        a = tA[i]
        b = tB[i]
        c = a * b
        pairwise_products.append(c)

    t = (n, sum(pairwise_products))
    return t


# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)   
print(dot_product(tA, tB)) # prints (3,32)
