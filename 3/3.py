def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if n == 0:
        return 0
    else:
        return m + multiply(m, n - 1)

# def multiply2(m, n, prod_so_far=0):
#     """ Takes two positive integers and returns their product using recursion.
#     >>> multiply2(5, 3)
#     15
#     """
#     if n == 0:
#       return prod_so_far
#     else:
#       return multiply2(m, n - 1, m + prod_so_far)






























def multiply(m, n):
    if n == 1:
        return m
    return m + multiply(m, n - 1)
