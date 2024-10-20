from collections import Counter
from typing import List

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        Frequency = Counter(nums)
        for f in Frequency.values():
            if f > 2:
                return False
        return True

# Test the function with some cases
def test_isPossibleToSplit():
    solution = Solution()
    
    # Test case 1: No number appears more than twice
    nums1 = [1, 2, 2, 3, 1]
    print(f"Test case 1: {nums1} -> {solution.isPossibleToSplit(nums1)}")  # Expected output: True
    
    # Test case 2: A number appears more than twice
    nums2 = [1, 2, 2, 3, 3, 3, 1]
    print(f"Test case 2: {nums2} -> {solution.isPossibleToSplit(nums2)}")  # Expected output: False
    
    # Test case 3: Single number appears once
    nums3 = [5]
    print(f"Test case 3: {nums3} -> {solution.isPossibleToSplit(nums3)}")  # Expected output: True
    
    # Test case 4: Empty list
    nums4 = []
    print(f"Test case 4: {nums4} -> {solution.isPossibleToSplit(nums4)}")  # Expected output: True
    
    # Test case 5: All numbers appear exactly twice
    nums5 = [4, 4, 6, 6, 9, 9]
    print(f"Test case 5: {nums5} -> {solution.isPossibleToSplit(nums5)}")  # Expected output: True

if __name__ == "__main__":
    test_isPossibleToSplit()
    print("All test cases passed!")