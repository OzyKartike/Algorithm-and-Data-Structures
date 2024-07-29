class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dictionary = {}
        for num in nums:
            dictionary[num] = dictionary.get(num,0) + 1
        for key,value in dictionary.items():
            if (value & 1):
                return False
        return True
