class Solution:
    def shortestPalindrome(self, s: str) -> str:
        start =  len(s)-1
        n = start-1
        rs = s
        while rs[::-1] != rs:
            rs = s[start:n: -1]+s
            n -= 1 
        return rs
