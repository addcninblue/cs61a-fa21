from functools import reduce

def map_strict(fn, iterable):
    """
    Mimics Python's `map` by using reduce. In contrast to `map`, this returns the list itself instead of a iterable.

    >>> map_strict(lambda x: x * x, [1,2,3])
    [1, 4, 9]
    """
    return reduce(lambda lst_so_far, elem: lst_so_far + [fn(elem)], iterable, [])

def filter_strict(pred, iterable):
    """
    Mimics Python's `filter` by using reduce. In contrast to `filter`, this returns the list itself instead of a iterable.

    >>> filter_strict(lambda x: x % 2 == 1, [1,2,3])
    [1, 3]
    """
    return reduce(lambda lst_so_far, elem: lst_so_far + [elem] if pred(elem) else lst_so_far, iterable, [])
