class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            k = (i+nums[i])%len(nums)
            ans[i] = nums[k]
        return ans