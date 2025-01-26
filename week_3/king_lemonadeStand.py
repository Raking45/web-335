""" 
    Title: king_lemonadeStand.py
    Author: Robert King
    Date: January 25, 2025
    Description: A simple program that calculates the profit from selling lemonade.
"""
#Calculate the total cost of making lemonade.
def calculate_cost(lemons_cost, sugar_cost):
    return lemons_cost + sugar_cost

#Calculate the profit from selling lemonade.
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    total_cost = lemons_cost + sugar_cost
    return selling_price - total_cost

#Variables
lemons_cost = 7.90
sugar_cost = 4.99
selling_price = 39.80

#Calculate the total cost and profit.
total_cost = calculate_cost(lemons_cost, sugar_cost)
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

#Output variables using concatenated string.
cost_result = f"{lemons_cost} + {sugar_cost} = {total_cost:.2f}"
profit_result = f"The profit from selling the lemonade is ${selling_price} - {total_cost:.2f} = {profit:.2f}"

#Results printed to console using output variables in a concatenated string.
output = "Cost Calculation: " + cost_result + "\n" + "Profit Calculation: " + profit_result
print(output)