# Gradient Descent

x = 2
lr = 0.1
iterations = 100

for i in range(iterations):

    dy = 2 * (x + 3)

    x = x - lr * dy

    if i % 10 == 0:
        print("Iteration:", i, "X:", x)

y = (x + 3)**2

print("Minimum X:", x)
print("Minimum Y:", y)