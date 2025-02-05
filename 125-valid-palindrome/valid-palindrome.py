class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ""
        for i in range(len(s)-1, -1, -1):
            if s[i].isalnum():
                rev += s[i]
        rev = rev.lower()
        return rev == rev[::-1]