class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        flag = False
        for numOne in arr1:
            flag = False
            for numTwo in arr2:
                if abs(numOne - numTwo) <= d:
                    flag = True
            if flag == False:
                count+= 1
                print(numOne)
        return count
