def square(x):
    return x * x

def change_square():
    global square
    square = lambda x: x
    return 2

print(square(change_square())) # Note `square` is original
print(square(3))               # Note `square` is now identity function

# Solution with ceil, from classmate. It works!
def is_prime(n):
    import math
    x = math.ceil(math.sqrt(n))
    while x <= n-1:
        if n % x == 0:
            return False
        x += 1
    return True

