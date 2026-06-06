class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sM = {}
        tM = {}
        if len(s) != len(t):
            return False
        for x in range(len(s)):
            if s[x] in sM:
                sM[s[x]] += 1
            else:
                sM[s[x]] = 1
            if t[x] in tM:
                tM[t[x]] += 1
            else:
                tM[t[x]] = 1
        if tM == sM:
            return True
        return False