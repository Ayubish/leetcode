class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        counter = 1
        for k in range(len(nums)):
            if k>0 and nums[k]==nums[k-1]:
                continue
            if nums[k]>0:
                if nums[k]!=counter:
                    return counter
                counter+=1
        return nums[-1]+1 if nums[-1] >0 else 1