# def count_stair_ways(n):
#     """Returns the number of ways to climb up a flight of
#     n stairs, moving either 1 step or 2 steps at a time.
#     >>> count_stair_ways(4)
#     5
#     """
#     if n == 1 or n == 2:
#         return n
#     return count_stair_ways(n-1) + count_stair_ways(n-2)

def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_stair_ways(n-1) + count_stair_ways(n-2)

def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    def helper(s):
        if s == 1:
            return count_k(n-s, k)
        return count_k(n-s, k) + helper(s-1)
    if n < 0:
        return 0
    if n == 0:
        return 1
    return helper(k)


# nested_lists = [1, [2, 3], [4, [5]]]
# a = nested_lists[1]
# a.append(4)
# nested_lists

# nested_lists = [1, [2, 3], [4, [5]]]
# my_copy = nested_lists[:] # Defaults to [0:len(nested_lists)]
# my_copy[1].append(4)
# nested_lists

a = [1, 5, 4, [2, 3], 3]
print(a[0], a[-1])

len(a)

2 in a

a[3][0]

# def even_weighted(s):
#     return [i * s[i] for i in range(len(s)) if i % 2 == 0]

# def even_weighted(s):
#     return [v * i for i, v in enumerate(s) if i % 2 == 0]

def even_weighted(s):
    return [e * s.index(e) for e in s if s.index(e) % 2 == 0]
