class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        longest = 0
        win = ""
        while right<=len(s):
            win = s[left:right]
            if len(win)==len(set(win)):
                right+=1
            else:
                longest = max(longest, len(win)-1)
                left+=1
        
        return max(longest, len(set(win)))