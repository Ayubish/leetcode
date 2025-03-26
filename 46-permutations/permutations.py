class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def backtrack(perm, arr):
            if len(arr) == 0:
                ans.add(tuple(perm))
                return 
            for i, num in enumerate(arr):
                backtrack(perm[:] + [num], arr[:i]+arr[i+1:])
            return
        backtrack([], nums)
        return list(ans)
        