class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = []
        zeros = []
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                nums[i-1]=2*nums[i]
                nums[i] = 0
        for num in nums:
            if num == 0:
                zeros.append(num)
            else:
                ans.append(num)
        return ans + zeros