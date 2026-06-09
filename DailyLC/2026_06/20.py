class Solution:
    def isValid(self, s: str) -> bool:
        parenthesisChar = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if stack and c in parenthesisChar:
                if stack.pop() != parenthesisChar[c]:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        return False
                