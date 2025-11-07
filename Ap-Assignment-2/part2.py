def pearson_corr(xs, ys):
    # pass 1: mean
    itx, ity = iter(xs), iter(ys)
    n = 0
    sx = 0.0
    sy = 0.0
    while True:
        try:
            x = next(itx)
            y = next(ity)
        except StopIteration:
            break
        sx += x
        sy += y
        n += 1
    if n == 0:
        return None
    mx = sx / n
    my = sy / n

    # pass 2: sums
    itx, ity = iter(xs), iter(ys)
    sxx = syy = sxy = 0.0
    while True:
        try:
            x = next(itx)
            y = next(ity)
        except StopIteration:
            break
        dx = x - mx
        dy = y - my
        sxx += dx * dx
        syy += dy * dy
        sxy += dx * dy

    # check variance
    if sxx == 0 or syy == 0:
        return None

    # r = cov / (std_x * std_y)
    r = sxy / ((sxx ** 0.5) * (syy ** 0.5))
    return r


# Example
xs = [1, 2, 3, 4, 5]
ys = [2, 4, 6, 8, 10]
print(pearson_corr(xs, ys))  # ≈ 1.0
