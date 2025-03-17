class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        prefix = [0]*(n+1)

        for i in range(n):
            prefix[i+1] = prefix[i]+nums[i]
        
        dic = defaultdict(int)
        ans = 0
        
        for i in prefix:
            if i-goal in dic:
                ans += dic[i-goal]
            dic[i] += 1
        return ans
        