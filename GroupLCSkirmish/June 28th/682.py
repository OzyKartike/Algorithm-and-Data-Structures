class Solution:
    def calPoints(self, operations: List[str]) -> int:
        finalArr = []
        for operator in operations:
            if operator.isdigit() or operator[0] == '-':
                finalArr.append(int(operator))
            elif operator == 'C':
                finalArr.pop()
            elif operator == 'D':
                x = int(finalArr[-1])*2
                finalArr.append(x)
            elif operator == '+':
                finalArr.append(int(finalArr[-1]) + int(finalArr[-2]))
        return sum(finalArr)
