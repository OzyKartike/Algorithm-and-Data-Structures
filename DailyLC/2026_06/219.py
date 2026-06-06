class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}
        if nums is None:
            return False
        for x, a in enumerate(nums):
            if a in hm and x-hm[a]<=k:
                return True
            else:
                hm[a] = x
        return False