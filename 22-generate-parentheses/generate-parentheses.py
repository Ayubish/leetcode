class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(par, i):
            if i+len(par) == 2*n:
                par += ")"*i
                ans.add(par)
                return
            
            backtrack(par+"(", i+1)
            if i > 0:
                backtrack(par+")", i-1)
            return
        ans = set()
        backtrack("(", 1)
        return list(ans)