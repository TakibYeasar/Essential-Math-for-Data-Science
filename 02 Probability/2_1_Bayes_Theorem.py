# Example 2-1. Using Bayes’ Theorem in Python

p_coffee_drinker = .65
p_cancer = .005
p_coffee_drinker_given_cancer = .85
p_cancer_given_coffee_drinker = p_coffee_drinker_given_cancer * p_cancer / p_coffee_drinker

print(p_cancer_given_coffee_drinker)
