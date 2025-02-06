class Solution:
    def printVertically(self, s: str) -> List[str]:
        a = s.split()
        ans = []
        maxlen = sorted(a, key=len)[-1]
        for i in range(len(maxlen)):
            row = ""
            for word in a:
                if i<len(word):
                    row += word[i]
                else:
                    row += " "
            ans.append(row.rstrip())
        return ans