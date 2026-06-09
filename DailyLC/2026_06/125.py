class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = s.lower().strip().replace(" ", "")
        newStr = ""
        for c in palindrome:
            if c.isalnum():
                newStr += c
        if newStr == newStr[::-1]:
            return True
        else:
            return False