class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        if nums is None:
            return False
        for i in range(len(nums)):
            if nums[i] in hs:
                return True
            hs.add(nums[i])
        return False