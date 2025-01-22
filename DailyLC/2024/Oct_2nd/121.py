from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for price in prices:
            profit = max(profit, price - lowest)
            lowest = min(lowest, price)
        return profit

def test_maxProfit():
    solution = Solution()
    
    # Test cases
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
    assert solution.maxProfit([5]) == 0
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_maxProfit()

