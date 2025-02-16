class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k>len(nums):
            k = k%len(nums)
        nums[0:] = nums[-k:]+nums[0:-k]