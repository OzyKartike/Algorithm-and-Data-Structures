class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()
        
        mask = (1 << bit_length) - 1
        
        return num ^ mask
    


if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    assert solution.findComplement(5) == 2
    assert solution.findComplement(1) == 0
    assert solution.findComplement(10) == 5
    assert solution.findComplement(0) == 1
    
    print("All test cases passed!")