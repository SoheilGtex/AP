# best algorithm: linear scan for second largest
def second_largest_linear(a):
    n = len(a)
    if n < 2:
        return None
    max1 = None
    max2 = None
    for x in a:
        if max1 is None:
            max1 = x
        elif x > max1:
            max2 = max1
            max1 = x
        elif x < max1:
            if max2 is None or x > max2:
                max2 = x
    return max2


# worst algorithm: selection sort then take second largest
def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        if min_index != i:
            temp = a[i]
            a[i] = a[min_index]
            a[min_index] = temp

def second_largest_via_sort(a):
    n = len(a)
    if n < 2:
        return None
    b = a[:]
    selection_sort(b)
    return b[n - 2]
