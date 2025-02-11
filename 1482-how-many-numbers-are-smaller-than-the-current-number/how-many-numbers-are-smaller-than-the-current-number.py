class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        ans = []
        for num in nums:
            count = 0
            i=0
            while sorted_nums[i]<num:
                count += 1
                i+=1
            ans.append(count)
        return ans