---
author: CS61A Review - Recursion
date: 2021-12-10
styles:
  style: solarized-dark
---

# Recursion

Today:
* Recursion
  * Recursion
    * Recursion
      * Recursion
        * ...

---

# Recursion

Recall:

Recursion is a way of solving a big problem by breaking it down into smaller subproblems **of the same nature**. (This means the *implementation* of the function is written *in terms of itself*.)

Example: `factorial`. Whiteboard -->

---

# Recursion, a 3-step guide

1. **Base case.** You can think of the base case as the case of the simplest function input, or as the stopping condition for the recursion.
2. **Recursive call on a smaller problem.** You can think of this step as calling the function on a smaller problem that our current problem depends on. We assume that a recursive call on this smaller problem will give us the expected result; we call this idea the "recursive leap of faith".
3. **Solve the larger problem.** In step 2, we found the result of a smaller problem. We want to now use that result to figure out what the result of our current problem should be, which is what we want to return from our current function call.

For those of you familiar, think **Induction**. (It's the exact same concept!)

---

# Warmup. G Function.

A mathematical function `G` on positive integers is defined by two cases:

```
G(n) = n,                                       if n <= 3
G(n) = G(n - 1) + 2 * G(n - 2) + 3 * G(n - 3),  if n > 3
```

Write a recursive function `g` that computes `G(n)`. Then, write an iterative
function `g_iter` that also computes `G(n)`. Lastly, write a recursive
implementation of `G(n)` that runs in linear time with respect to `n`.

> *Hint:* The `fibonacci` example in the [tree recursion
> lecture][tree-recursion] is a good illustration of the relationship between
> the recursive and iterative definitions of a tree recursive problem.

> *Hint:* For the last, consider a helper function.

---

# G Function Solution

```py
def g(n): # Recursive
    if n in (1, 2, 3):
        return n
    return g(n-1) + 2*g(n-2) + 3*g(n-3)

def g_iter(n): # Iterative
    if n == 1 or n == 2 or n == 3:
        return n
    a, b, c = 1, 2, 3
    while n > 3:
        a, b, c = b, c, c + 2*b + 3*a
        n = n - 1
    return c

def g_linear(n): # Recursive, linear time
    if n in (1, 2, 3):
        return n
    def helper(curr, prev, prev_2, n):
        if n == 0:
            return curr
        return helper(
            curr + 2*prev + 3*prev_2,
            curr,
            prev,
            n-1
        )
    return helper(3, 2, 1, n-3)
```

---

# Jump Game

Consider a variation on the staircases problem. Instead of taking a fixed
amount of stairs `k` at a time, we now have an array where each index `i` of
the array represents the maximum amount of steps we can take at step `i`.
Return whether we can reach the last index of this array.

Bonus: do this in no worse than quadratic time.

```py
def valid_path(nums):
    """
    >>> valid_path([3, 2, 1, 1, 0])
    True
    >>> valid_path([1, 0, 0])
    False
    """
    # YOUR SOLUTION HERE
```

---

# Jump Game Solution

```py
def valid_path(nums):
    """
    >>> valid_path([3, 2, 1, 1, 0])
    True
    >>> valid_path([1, 0, 0])
    False
    """
    if len(nums) == 1:
        return True
    elif len(nums) == 0:
        return False
    elif nums[0] == 0:
        return False
    return any(valid_path(nums[i:]) for i in range(1, nums[0]+1))
```

---

# Max Subsequence

A subsequence of a number is a series of (not necessarily contiguous) digits of the number.
For example, 12345 has subsequences that include 123, 234, 124, 245, etc. Your task is to get
the maximum subsequence below a certain length.

```py
def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are
        [2, 0, 1, 2, 5, 20, 21, 22, 25, 01, 02, 05, 12, 15, 25, 201, 202, 205, 212, 215,
        225, 012, 015, 025, 125]
    and of these, the maxumum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    # YOUR SOLUTION HERE
```

---

# Max Subsequence Solution

A subsequence of a number is a series of (not necessarily contiguous) digits of the number.
For example, 12345 has subsequences that include 123, 234, 124, 245, etc. Your task is to get
the maximum subsequence below a certain length.

```py
def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are
        [2, 0, 1, 2, 5, 20, 21, 22, 25, 01, 02, 05, 12, 15, 25, 201, 202, 205, 212, 215,
        225, 012, 015, 025, 125]
    and of these, the maxumum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    if n == 0 or t == 0:
        return 0
    with_last = max_subseq(n // 10, t - 1) * 10 + n % 10
    without_last = max_subseq(n // 10, t)
    return max(with_last, without_last)
```

---

# Ten Pairs

Write a function that takes a positive integer `n` and returns the
number of ten-pairs it contains.  A ten-pair is a pair of digits
within `n` that sums to 10.   *Do not use any assignment statements.*

The number 7,823,952 has 3 ten-pairs. The first and fourth digits sum
to 7+3=10, the second and third digits sum to 8+2=10, and the second
and last digit sum to 8+2=10. Note that a digit can be part of more than
one ten-pair.

> *Hint*: Use a helper function to calculate how many times a digit
appears in n.

```py
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    # YOUR SOLUTION HERE
```

---

# Ten Pairs Solution

```py
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    # BEGIN SOLUTION
    if n < 10:
        return 0
    else:
        return ten_pairs(n//10) + count_digit(n//10, 10 - n%10)

def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5)
    4
    """
    if n == 0:
        return 0
    else:
        if n%10 == digit:
            return count_digit(n//10, digit) + 1
        else:
            return count_digit(n//10, digit)
    # END SOLUTION
```

---

# Full Binary Tree

A **full binary tree** is a tree where each node has either 2 branches or 0 branches, but never 1 branch.

Write a function which returns the number of unique full binary tree structures that have exactly n leaves.

For those interested in combinatorics, this problem does have a [closed
form solution](http://en.wikipedia.org/wiki/Catalan_number)):

```py
def num_trees(n):
    """Returns the number of unique full binary trees with exactly n leaves. E.g.,

    1   2        3       3    ...
    *   *        *       *
       / \      / \     / \
      *   *    *   *   *   *
              / \         / \
             *   *       *   *

    >>> num_trees(1)
    1
    >>> num_trees(2)
    1
    >>> num_trees(3)
    2
    >>> num_trees(8)
    429

    """
    # YOUR SOLUTION HERE
```

---

# Full Binary Tree Solution

```py
def num_trees(n):
    """Returns the number of unique full binary trees with exactly n leaves. E.g.,

    1   2        3       3    ...
    *   *        *       *
       / \      / \     / \
      *   *    *   *   *   *
              / \         / \
             *   *       *   *

    >>> num_trees(1)
    1
    >>> num_trees(2)
    1
    >>> num_trees(3)
    2
    >>> num_trees(8)
    429

    """
    if n == 1:
        return 1
    return sum(num_trees(k) * num_trees(n-k) for k in range(1, n))
```

---

# Bonus Q; Solution Included!

A palindrome is a word spelled the same forwards and backwards. Find the
longest substring of `word` such that the substring is a palindrome.

Ignore everything after docstring if you don't want to look at the solution.

```py
def longest_palindrome(word):
    """
    >>> longest_palindrome("racecar")
    "racecar"
    >>> longest_palindrome("mmmmmmm")
    "mmmmmm"
    >>> longest_palindrome("hello")
    "ll"
    """
    def helper(word, must_end_with):
        if len(word) < len(must_end_with) or len(word) == 0:
            return ""
        possibilities = []
        if word[:len(must_end_with)] == must_end_with:
            possibilities.append(must_end_with[::-1] + must_end_with)
        elif word[1:len(must_end_with)+1] == must_end_with:
            possibilities.append(must_end_with[::-1] + word[:len(must_end_with)+1])
        return max([helper(word[1:], must_end_with), helper(word[1:], word[0] + must_end_with)] + possibilities, key=len)
    return helper(word, "")
```

---

# Credits:

* Jump Game is from Leetcode.
* Palindrome is from Leetcode.
