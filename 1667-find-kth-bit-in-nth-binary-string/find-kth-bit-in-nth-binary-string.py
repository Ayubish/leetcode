class Solution:
    def reverse(self, s):
        ans = []
        for c in s:
            if c == "0":
                ans.append("1")
            else:
                ans.append("0")
        ans.reverse()
        return "".join(ans)
    def helper(self, s, n , count):
        if count == n:
            return s
        return self.helper(s+"1"+self.reverse(s), n, count+1)
    def findKthBit(self, n: int, k: int) -> str:
        s = self.helper("0", n-1, 0)
        return s[k-1]