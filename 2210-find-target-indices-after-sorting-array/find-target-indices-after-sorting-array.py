class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        flag = False
        for i in range(len(nums)):
            if nums[i]==target:
                ans.append(i)
                flag = True
            elif flag:
                break
        return ans