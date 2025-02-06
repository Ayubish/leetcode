class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0]*len(s)
        for i in range(len(s)):
            place = indices[i]
            ans[place]=s[i]
        return ''.join(ans)