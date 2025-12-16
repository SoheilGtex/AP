# =========================
# 1) Simple Linear Regression (manual) : Sales ~ TV
# =========================

import pandas as pd

df = pd.read_csv("/mnt/data/advertising.csv")

x = df["TV"].to_list()
y = df["Sales"].to_list()
n = len(x)

# Means
x_mean = sum(x) / n
y_mean = sum(y) / n

# Least-squares slope/intercept (manual)
num = 0.0  # covariance part
den = 0.0  # variance part
for xi, yi in zip(x, y):
    num += (xi - x_mean) * (yi - y_mean)
    den += (xi - x_mean) ** 2

b1 = num / den
b0 = y_mean - b1 * x_mean

print("Linear: Sales = b0 + b1*TV")
print("b0 =", b0)
print("b1 =", b1)

# Example prediction
tv_new = 100
print("Pred Sales (TV=100):", b0 + b1 * tv_new)


# =========================
# 2) Simple Logistic Regression (manual GD) : HTN ~ BMI
# =========================

import math

df2 = pd.read_excel("/mnt/data/HNT.xlsx")

# Build BMI (kg / m^2)
bmi = []
for w, h in zip(df2["WEIGHT"].to_list(), df2["HEIGHT"].to_list()):
    bmi.append(w / ((h / 100) ** 2))

y2 = df2["HTN"].to_list()
n2 = len(bmi)

# Standardize x for easier GD
x_mean2 = sum(bmi) / n2
x_std2 = (sum((xi - x_mean2) ** 2 for xi in bmi) / n2) ** 0.5
x2 = [(xi - x_mean2) / x_std2 for xi in bmi]

def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))

# Weights
w0, w1 = 0.0, 0.0

# Gradient Descent
lr = 0.1
steps = 5000

for _ in range(steps):
    p = [sigmoid(w0 + w1 * xi) for xi in x2]
    dw0 = sum(pi - yi for pi, yi in zip(p, y2)) / n2
    dw1 = sum((pi - yi) * xi for pi, yi, xi in zip(p, y2, x2)) / n2
    w0 -= lr * dw0
    w1 -= lr * dw1

print("\nLogistic: P(HTN=1) = sigmoid(w0 + w1*BMI_std)")
print("w0 =", w0)
print("w1 =", w1)

# Example probability
bmi_new = 32
x_new = (bmi_new - x_mean2) / x_std2
p_new = sigmoid(w0 + w1 * x_new)
print("Pred P(HTN=1) for BMI=32:", p_new)
