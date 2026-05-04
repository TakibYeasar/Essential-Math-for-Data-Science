# Example 5-14. Using Pandas to see the correlation coefficient between every pair of variables
import pandas as pd

# Read data into Pandas dataframe
df = pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",")
# Print correlations between variables
correlations = df.cor
