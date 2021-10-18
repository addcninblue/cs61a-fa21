def apply_op(op, arg1, arg2):
    OPS = {
        "*": lambda x, y: x * y,
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y
    }
    return OPS[op](arg1, arg2)

def gen_ways_to_compute(numbers: List[int], operators: List[str]) -> List[int]:
    """
    Takes in a list of numbers and a list of operators, and yields all possible
    combinations of outputs by placing parentheses at any valid location. Order
    does NOT matter.
    Example:

    >>> # Explanation for below:
    >>> # (2*(3-(4*5))) = -34
    >>> # ((2*3)-(4*5)) = -14
    >>> # ((2*(3-4))*5) = -10
    >>> # (2*((3-4)*5)) = -10
    >>> # (((2*3)-4)*5) = 10
    >>> sorted(list(gen_ways_to_compute([2, 3, 4, 5], ["*", "-", "*"])))
    [-34, -14, -10, -10, 10]
    """
    if ______________:
        ___________________
    for ___________________:
        for ___________________:
            for ___________________:
                ___________________
