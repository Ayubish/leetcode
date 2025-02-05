class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sub = s.split()
        return len(sub[-1])