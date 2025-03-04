class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)-1):
            maxReach = max(maxReach, i+nums[i])
            if i==maxReach:
                return False
        return True
                