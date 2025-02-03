class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_n = max(nums)
        list_set = set(nums)
        for i in range(max_n+1):
            if i not in list_set:
                return i
        return max_n+1