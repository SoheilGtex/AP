def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f

def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

n = int(input("Enter N: "))
k = int(input("Enter K: "))

if k > n or k < 0:
    print("Invalid")
else:
    print(combination(n, k)) 
