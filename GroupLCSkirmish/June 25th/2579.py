class Solution:
    def coloredCells(self, n: int) -> int:
        # 1 ; 1 ; 4
        # 2 ; 5 ; 8
        # 3 ; 13; 12
        # 4 ; 25 ; 16
        add = 0
        ans = 1
        for i in range(1,n):
            add += 4
            ans += add
        return ans
