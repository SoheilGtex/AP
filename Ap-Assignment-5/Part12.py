#part1

def euclidean_distance(x1, x2):
    s = 0.0
    for i in range(len(x1)):
        d = x1[i] - x2[i]
        s += d * d
    return s ** 0.5


def knn_predict(train_X, train_y, x, k):
    distances = []
    for i in range(len(train_X)):
        d = euclidean_distance(train_X[i], x)
        distances.append((d, train_y[i]))
    distances.sort(key=lambda t: t[0])
    counts = {}
    for i in range(k):
        label = distances[i][1]
        if label in counts:
            counts[label] += 1
        else:
            counts[label] = 1
    best_label = None
    best_count = -1
    for label in counts:
        if counts[label] > best_count:
            best_count = counts[label]
            best_label = label
    return best_label


train_X = [
    [1.0, 2.0],
    [1.5, 1.8],
    [5.0, 8.0],
    [6.0, 9.0],
    [1.0, 0.6],
    [9.0, 11.0],
]

train_y = [
    "A",
    "A",
    "B",
    "B",
    "A",
    "B",
]

k = int(input("Enter K: "))

raw = input("Enter features of sample (space separated): ")
x = []
for v in raw.split():
    x.append(float(v))

pred = knn_predict(train_X, train_y, x, k)
print("Predicted class:", pred)


#part2


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
