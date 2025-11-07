# nums can be a list or tuple of numbers
def count_items(nums):
    # manual length
    c = 0
    for _ in nums:
        c += 1
    return c

def compute_min(nums):
    # min without built-ins
    it = iter(nums)
    try:
        m = next(it)
    except StopIteration:
        return None
    for x in it:
        if x < m:
            m = x
    return m

def compute_max(nums):
    # max without built-ins
    it = iter(nums)
    try:
        M = next(it)
    except StopIteration:
        return None
    for x in it:
        if x > M:
            M = x
    return M

def compute_mean(nums):
    # average = total / count
    total = 0.0
    n = 0
    for x in nums:
        total += x
        n += 1
    if n == 0:
        return None
    return total / n

def second_largest_distinct(nums):
    # second largest DISTINCT value
    first = None
    second = None
    for x in nums:
        if first is None or x > first:
            if first is not None and x != first:
                second = first
            first = x
        elif x != first and (second is None or x > second):
            second = x
    return second

def numbers_below_mean(nums):
    # numbers < mean
    mu = compute_mean(nums)
    if mu is None:
        return None
    out = []
    for x in nums:
        if x < mu:
            out.append(x)
    return out

def std_dev_population(nums):
    # population std: sqrt( sum((x - mu)^2) / n )
    mu = compute_mean(nums)
    if mu is None:
        return None
    n = 0
    sse = 0.0
    for x in nums:
        d = x - mu
        sse += d * d
        n += 1
    if n == 0:
        return None
    return (sse / n) ** 0.5

# ---- example ----
nums = [7, 2, 9, 9, 4, 1, 6]

print("count:", count_items(nums))
print("max:", compute_max(nums))
print("min:", compute_min(nums))
print("mean:", compute_mean(nums))
print("second largest (distinct):", second_largest_distinct(nums))
print("numbers < mean:", numbers_below_mean(nums))
print("std dev (population):", std_dev_population(nums))
