from functools import lru_cache

@lru_cache(maxsize=None)
def fib_recur(nterm):
    # base case
    if nterm == 0 or nterm == 1:
        return nterm
    
    # recursive case
    return fib_recur(nterm-1) + fib_recur(nterm-2)

print(fib_recur(7))