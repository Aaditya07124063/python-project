def subset_sum_backtrack(arr, target, index=0, current_subset=[], solutions=[]):
    if sum(current_subset) == target:
        solutions.append(current_subset[:])
        return
    if sum(current_subset) > target or index >= len(arr):
        return
    current_subset.append(arr[index])
    subset_sum_backtrack(arr, target, index + 1, current_subset, solutions)
    current_subset.pop()
    subset_sum_backtrack(arr, target, index + 1, current_subset, solutions)
    return solutions

def knapsack_backtrack(weights, values, capacity, index=0, current_weight=0, current_value=0, selected_items=[], best_solution=[0, []]):
    if current_weight <= capacity and current_value > best_solution[0]:
        best_solution[0] = current_value
        best_solution[1] = selected_items[:]
    if index >= len(weights) or current_weight > capacity:
        return
    selected_items.append(index)
    knapsack_backtrack(weights, values, capacity, index + 1, current_weight + weights[index], current_value + values[index], selected_items, best_solution)
    selected_items.pop()
    knapsack_backtrack(weights, values, capacity, index + 1, current_weight, current_value, selected_items, best_solution)
    return best_solution[1]

arr = [5, 10, 12, 13, 15, 18]
target = 30
print("Subsets with sum 30:")
print(subset_sum_backtrack(arr, target))

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print("Best items for knapsack:")
print(knapsack_backtrack(weights, values, capacity))
