'''

Date : Feb 14, 2026

This is Fractional knapsack algorithm solved using greedy approach.
Here, instead of excluding entire weight,
we take fraction of weights to meet desired weight limit and assign remaining weight as 0.

The fractional knapsack problem allows taking portions of items.
The optimal solution is achieved using a greedy algorithm that prioritizes items with the highest value-to-weight ratio.
'''

def fractional_knapsack(weight,profit,capacity):

    lst = []
    for i in range(len(weights)):
        lst.append((weights[i], profit[i], profit[i] / weights[i]))

    lst.sort(key = lambda x : x[2],reverse = True) #[(10, 60, 6.0), (20, 100, 5.0), (30, 120, 4.0)]

    maximum_capacity = capacity

    total_profit = 0.0
    for weight,profit,ratio in lst:
        if weight <= maximum_capacity:
            total_profit += profit
            maximum_capacity -= weight
        else:
            remain_weight = maximum_capacity / weight
            total_profit += profit * remain_weight
            maximum_capacity = 0
            break
    return total_profit

if __name__ == "__main__":
    weights = [10, 20, 30]
    profit = [60, 100, 120]
    capacity = 50
    max_profit = fractional_knapsack(weights,profit,capacity)
    print(f"Maximum value for Fractional Knapsack: {max_profit}")
