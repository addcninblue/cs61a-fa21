def f(x):
    return x * 2

def g(x):
    return x + 1

x = 3
x, y = f(x), g(x) # simultaneous assignment

def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n + k)
    return next_sum

# Doesn't work:
print_sums = print_sums(10) # prints 10
print_sums = print_sums(12) # infinite recursion

# Works:
f = print_sums(10) # prints 10
f = f(12) # prints 22

# To understand why, use PythonTutor for the above!


def f(x):
    return 1

def f(x, y):
    return 2

# f is now f(x, y)
