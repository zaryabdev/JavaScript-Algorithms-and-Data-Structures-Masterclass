def house_robber(money: list[int]) -> int:
    """
    Determines the maximum amount of money that can be robbed without alerting the police,
    considering that houses are arranged in a circle.

    Args:
        money (list[int]): List of amounts of money in each house.

    Returns:
        int: The maximum amount of money that can be robbed.
    """
    # Initialize memoization dictionaries for the two cases
    memo1 = {}  # Memo for excluding the first house
    memo2 = {}  # Memo for excluding the last house

    # Calculate the maximum money if the first house is excluded
    wout_first_house = _house_robber(money, 1, len(money), memo1)

    # Calculate the maximum money if the last house is excluded
    wout_last_house = _house_robber(money, 0, len(money) - 1, memo2)

    # Return the maximum of the two calculated values
    return max(wout_first_house, wout_last_house)

def _house_robber(money: list[int], start: int, end: int, memo: dict[int, int]) -> int:
    """
    Helper function to recursively find the maximum amount of money that can be robbed.

    Args:
        money (list[int]): List of amounts of money in each house.
        start (int): Starting index for the current subproblem.
        end (int): Ending index for the current subproblem (exclusive).
        memo (dict[int, int]): Memoization dictionary to store results of subproblems.

    Returns:
        int: The maximum amount of money that can be robbed for the current subproblem.
    """
    # Check if the result for this subproblem is already computed
    if start in memo:
        return memo[start]
    
    # Base case: If the starting index is greater than or equal to the end index
    # If there are no houses in the sub-range
    if start >= end:
        return 0
    
    # Option 1: Include the current house's money and move to the house two steps ahead(exclude the next one (start+1))
    include_first_amount = money[start] + _house_robber(money, start + 2, end, memo)

    # Option 2: Exclude the current house and move to the next house
    exclude_first_amount = _house_robber(money, start + 1, end, memo)

    # Memoize the result
    memo[start] = max(include_first_amount, exclude_first_amount)
    return memo[start]


# Time and Space Complexities

# - Time Complexity: O(n)
#   The time complexity is linear because each house is processed a constant number of times due to memoization.

# - Space Complexity: O(n)
#   The space complexity is linear due to the memoization dictionaries and the recursive call stack.

# Further Notes

# - Recursive Approach: This solution uses a recursive approach to solve the problem. At each step, the function decides whether 
# to include the current house's money or not and recursively solves the subproblems.
# - Circular Nature Handling: The problem of circular houses is handled by solving two separate subproblems:
#   1. Excluding the first house (i.e., considering houses from index 1 to the end).
#   2. Excluding the last house (i.e., considering houses from index 0 to the second last house).
# - Why Two Memos: Two separate memoization dictionaries are used to handle the two distinct subproblems (excluding the first house and excluding the last house) 
# to avoid conflicts in storing results(to prevent cross-contamination of memoized values).
# - Avoiding Slicing: Using start and end indices rather than slicing to create separate lists is more efficient as it avoids creating new list copies, reducing overhead and improving performance.
# - Edge Cases: The code handles the edge case where there is only one house by returning its value directly. Other edge cases include empty lists or lists with houses having zero money.

