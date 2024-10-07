def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

# Time complexity: O(2^n) since the func calls itself recursively n times
# Space complexity: O(n) since every call stack adds a frame