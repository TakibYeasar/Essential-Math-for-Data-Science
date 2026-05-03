# Example 1-6 shows how we can declare a mathematical function and iterate it in Python.

def f(x):
    return 2 * x + 1

x_values = [0, 1, 2, 3]

for x in x_values:
    y = f(x)
    print(y)