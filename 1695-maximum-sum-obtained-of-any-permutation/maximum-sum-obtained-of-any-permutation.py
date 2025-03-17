class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        MOD = 10**9 + 7

        for i,j in requests:
            prefix_sum[i] += 1
            prefix_sum[j + 1] -= 1
        
        for i in range(1,n+1):
            prefix_sum[i] += prefix_sum[i - 1]
        
        prefix_sum.sort(reverse = True)
        nums.sort(reverse = True)

        count = 0
        left = 0

        while prefix_sum[left] > 0:
            count += nums[left] * prefix_sum[left]
            left += 1
        
        return count % MOD