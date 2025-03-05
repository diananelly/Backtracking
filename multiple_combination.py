def shopping_csp(items, budget):
    """
    Optimized CSP solver with constraint propagation and memoization.

    :param items: List of tuples (item_name, price, max_quantity)
    :param budget: Available budget for shopping
    :return: List of valid combinations
    """
    result = []

    # Sort items by price (cheapest first for better budget management)
    items.sort(key=lambda x: x[1])

    # Memoization dictionary to store already computed subproblems
    memo = {}

    def backtrack(index, current_budget, current_combination):
        # If this state has been computed before, return the result from memo
        if (index, current_budget) in memo:
            return memo[(index, current_budget)]

        # If current_budget is 0, a valid combination is found
        if current_budget == 0:
            result.append(current_combination[:])
            return [current_combination[:]]

        # No more items to process
        if index >= len(items):
            return []

        item_name, price, max_quantity = items[index]

        # **Constraint Propagation: Reduce domain (max purchase based on budget)**
        max_purchase = min(max_quantity, current_budget // price)

        valid_combinations = []

        # Try different quantities from max purchase down to 0 (pruning larger first)
        for qty in range(max_purchase, -1, -1):
            new_budget = current_budget - (qty * price)

            # **Forward checking: Stop early if no budget remains**
            if new_budget < 0:
                break  # No valid purchase options, prune search

            current_combination.append((item_name, qty))  # Assign value
            valid_combinations.extend(backtrack(index + 1, new_budget, current_combination))  # Recurse
            current_combination.pop()  # Backtrack

        # Memoize the result for the current state
        memo[(index, current_budget)] = valid_combinations
        return valid_combinations

    # Start the backtracking process
    backtrack(0, budget, [])

    return result


# Example Usage
items = [("Chips", 5, float('inf')),  # Unlimited
         ("Soda", 3, float('inf')),  # Unlimited
         ("Cake", 10, 1),  # Max 1
         ("Balloons", 2, 2)]  # Max 2
budget = 20

shopping_combinations = shopping_csp(items, budget)
for combination in shopping_combinations:
    print(combination)
