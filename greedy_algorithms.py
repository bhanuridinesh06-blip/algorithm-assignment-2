# Task 3: Greedy Algorithms - Fractional Knapsack
def fractional_knapsack(items, capacity):
    # Sort items by value/weight ratio
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    
    total_value = 0.0
    for value, weight in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += value * (capacity / weight)
            break
    return total_value

# Test Data: (value, weight)
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50
print(f"Maximum value in Knapsack: {fractional_knapsack(items, capacity)}")
