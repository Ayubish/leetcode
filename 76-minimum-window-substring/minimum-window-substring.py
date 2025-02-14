class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(c1, c2):
            return len(c2-c1)==0

        tar = Counter(t)
        window = Counter()
        left = 0
        right = 0
        start = 0
        end = len(s)
        while right<len(s):
            window[s[right]]+=1
            while check(window, tar):
                if right-left<end-start:
                    start = left
                    end = right
                window[s[left]] -= 1
                left += 1
            right += 1
        if end==len(s):
            return ""
        return s[start:end+1]
            
# https://sharepad.io/live/IwQtJk4
# https://sharepad.io/live/yornZln