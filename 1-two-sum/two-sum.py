class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}
        for i in range(len(nums)):
            num_idx[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_idx and num_idx[diff] != i:
                return [i, num_idx[diff]]