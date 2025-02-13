class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        temp = set()
        while right<len(s):
            if s[right] not in temp:
                temp.add(s[right])
                right+=1
            else:
                longest = max(longest, len(temp))
                temp.remove(s[left])
                left+=1
        
        return max(longest, len(temp))