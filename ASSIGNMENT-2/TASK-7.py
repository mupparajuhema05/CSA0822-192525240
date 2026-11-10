def ways(n):
    if n <= 1:
        return 1
    a = b = 1
    for _ in range(2, n+1):
        a, b = b, a + b
return b
print("Ways for 5 steps :", ways(5))
print("Ways for 10 steps:", ways(10))
print("Ways for 30 steps:", ways(30))
