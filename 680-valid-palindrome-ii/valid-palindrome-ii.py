class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            rev = s[::-1]
            return s==rev
        left = 0
        right = len(s)-1
        while left<right:
            if s[left] != s[right] and right-1 != left:
                if isPalindrome(s[left+1:right+1]) or isPalindrome(s[left:right]):
                    return True
                else:
                    return False
            else:
                left += 1
                right -= 1
        return True