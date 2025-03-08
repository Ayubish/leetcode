class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i in range(len(nums)):
            if not stack or nums[stack[-1]]>nums[i]:
                stack.append(i)
        maxi = 0
        for j in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]]<=nums[j]:
                maxi = max(maxi, j-stack[-1])
                stack.pop()
        return maxi
        