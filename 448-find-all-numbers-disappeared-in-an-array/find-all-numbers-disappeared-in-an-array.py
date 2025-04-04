class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0 
        while i < len(nums):
            pos = nums[i] - 1
            if nums[i] == -1:
                i += 1
            elif pos != i:
                if nums[i] == nums[pos]:
                    nums[i] = -1
                    i += 1
                else:
                    nums[pos], nums[i] = nums[i], nums[pos]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] == -1:
                ans.append(i+1)
        return ans
