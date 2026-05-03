from scipy.stats import norm
# Example 3-10. The normal distribution CDF in Python
mean = 64.43
std_dev = 2.99
x = norm.cdf(64.43, mean, std_dev)
print(x)
