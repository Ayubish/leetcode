class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ref = Counter(nums)
        ans = [0,0]
        for i in range(1, len(nums)+1):
            if i not in ref:
                ans[1] = i
            elif ref[i] == 2:
                ans[0] = i
        return ans
            