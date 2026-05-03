# Example 1-14. Calculating continuous interest in Python
from math import exp

p = 100  # principal, starting amount
r = .20  # interest rate, by year
t = 2.0  # time, number of years

a = p * exp(r*t)
print(a)
