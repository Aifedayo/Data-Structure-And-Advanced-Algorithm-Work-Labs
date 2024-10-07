def factorial(n):
    if n == 0:
        return 1
    else:
        n * factorial(n-1)

# Time complexity: 0(n) Since the function calls itself recursively (n) times
# Space complexity: 0(n) Each recursive call adds a frame to the call stack