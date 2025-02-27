class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        maxi = 0
        while left < right:
            currMax = 0
            if height[left] < height[right]:
                currMax = (right-left)*height[left]
                left += 1
            else:
                currMax = (right-left)*height[right] 
                right -= 1
            maxi = max(maxi, currMax)
        return maxi