from functools import lru_cache
def ways_naive(n):
    if n <= 1:
        return 1
return ways_naive(n-1) + ways_naive(n-2)
@lru_cache(None)
def ways_memo(n):
    if n <= 1:
        return 1
return ways_memo(n-1) + ways_memo(n-2)
def ways_iter(n):
    if n <= 1:
        return 1
    a = b = 1
    for _ in range(2, n+1):
        a, b = b, a + b
return b
print("Naive (5):", ways_naive(5)
print("Memo  (5):", ways_memo(5))
print("Iter  (5):", ways_iter(5))
print("Iter (10):", ways_iter(10))
