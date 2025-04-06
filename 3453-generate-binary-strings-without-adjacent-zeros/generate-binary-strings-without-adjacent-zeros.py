class Solution:
    def validStrings(self, n: int) -> List[str]:
        def backtrack(s):
            if len(s) >= 2 and s[-2:] == "00":
                return
            if len(s) == n:
                ans.append(s)
                return
            backtrack(s+"1")
            backtrack(s+"0")

        ans = []
        backtrack("1")
        backtrack("0")
        return ans