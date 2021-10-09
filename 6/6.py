# WWPD: Mutability

a = [1, 2, 3]
a[1:3] = [4, 5]

# def add_this_many(x, el, s):
#     """ Adds el to the end of s the number of times x occurs in s.
#     >>> s = [1, 2, 4, 2, 1]
#     >>> add_this_many(1, 5, s)
#     >>> s
#     [1, 2, 4, 2, 1, 5, 5]
#     >>> add_this_many(2, 2, s)
#     >>> s
#     [1, 2, 4, 2, 1, 5, 5, 2, 2]
#     """
#     count = 0
#     for elem in s:
#         if elem == x:
#             count += 1
#     for _ in range(count):
#         s.append(el)

def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    # [s.append(el) for _ in range(s.count(x))]
    s.extend([el] * s.count(x))
