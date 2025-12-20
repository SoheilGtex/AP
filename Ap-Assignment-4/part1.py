# Q1 
# The inner loop multiplies y by 2 exactly i times, so y = 2^i.
# The outer loop adds this value to x for i = 0 to n−1.
#
# Therefore:
# x = 2^0 + 2^1 + ... + 2^(n−1) = 2^n − 1


# Q2
def is_perfect(n):
    s = 0
    i = 1
    while i < n:
        if n % i == 0:
            s += i
        i += 1
    return s == n

n = int(input("Q2) n: "))
if is_perfect(n):
    print(n)


# Q3
i = 0
while i < 4:
    j = 0
    while j < 4:
        print(5 + i - j, end=" ")
        j += 1
    print()
    i += 1


# Q4
A = []
i = 0
while i < 10:
    A.append(list(map(int, input().split())))
    i += 1

saddle = False
i = 0
while i < 10:
    row_min = min(A[i])
    j = 0
    while j < 10:
        if A[i][j] == row_min:
            k = 0
            ok = True
            while k < 10:
                if A[k][j] > A[i][j]:
                    ok = False
                k += 1
            if ok:
                saddle = True
        j += 1
    i += 1

if saddle:
    print("true")
else:
    print("false")


# Q5
def pow2(n):
    return 2 ** n

n = int(input("Q5) n: "))
print(pow2(n))
