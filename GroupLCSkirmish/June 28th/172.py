class Solution:
    def trailingZeroes(self, n: int) -> int:
        #3!
        #3*2*1 = 6
        #4!
        #4*3*2*1 = 24
        #5!
        #5*4*3*2*1 = 120
        #6!
        #6*5*4*3*2 = 720
        #7!
        #7*6*5*4*3*2 = 5040
        #10!
        #10*9*8*7*6*5*4*3*2
        #3628800
        # mainly we want to see how many jumps of 5 we can get 
        i = 5
        count = 0
        while n//i:
            count += n//i
            i *= 5
        return count
