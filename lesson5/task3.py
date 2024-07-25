def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = 5  
print(f" {n} {factorial_iterative(n)}")

