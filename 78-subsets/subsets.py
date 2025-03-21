class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, sol = [], []

        def backtrack(i):
            if i == len(nums):
                ans.append(sol[:])
                return
            
            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return ans