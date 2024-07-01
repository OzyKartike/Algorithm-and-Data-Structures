class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        check = 3
        for num in arr:
            if check == 0:
                return True
            elif num%2 != 0:
                check -= 1
            else:
                check = 3
        if check == 0:
                return True
        return False
            
