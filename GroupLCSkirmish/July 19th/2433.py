class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        #0101 5
        #0111 7
        #0010 2
        n = len(pref)
        res = [0]*n
        c = 0
        for x in range(n):
            res[x] = c ^ pref[x]
            c ^= res[x]
        return res
