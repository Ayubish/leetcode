class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mini = min(nums)
        maxi = max(nums)
        arr = [0]*(maxi-mini+1)
        for num in nums:
            arr[num-mini] += 1
        index = 0
        for i in range(len(arr)):
            while arr[i]>0:
                nums[index] = i+mini
                arr[i] -= 1
                index+=1
        return nums
