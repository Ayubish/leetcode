class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mono_increasing = deque()
        mono_decreasing = deque()
        left = 0
        ans = float("-inf")
        for right in range(len(nums)):

            while mono_increasing and mono_increasing[-1][0] > nums[right]:
                mono_increasing.pop()
            while mono_decreasing and mono_decreasing[-1][0] < nums[right]:
                mono_decreasing.pop()

            mono_decreasing.append([nums[right], right])
            mono_increasing.append([nums[right], right])
          
            while mono_decreasing[0][0] - mono_increasing[0][0] > limit:
                if left == mono_decreasing[0][1]:
                    mono_decreasing.popleft()
                elif left == mono_increasing[0][1]:
                    mono_increasing.popleft()
                left += 1
                
            ans = max(ans, right-left+1)
    
        return ans
            