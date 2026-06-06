class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, x in enumerate(nums):
            if target-x in hm:
                arr = [hm[target-x], i]
                return arr
            else:
                hm[x] = i
        return []