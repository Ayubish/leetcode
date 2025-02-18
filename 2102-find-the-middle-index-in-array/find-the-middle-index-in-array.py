class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre1 = []
        pre2 = []
        var = 0
        for num in nums:
            var += num
            pre1.append(var)
        var=0
        for i in range(len(nums)-1, -1, -1):
            var += nums[i]
            pre2.append(var)
        pre2 = pre2[::-1]
        print(pre1)
        print(pre2)
        for i in range(len(nums)):
            if len(nums)==1:
                return 0
            elif i==0:
                if pre2[i+1]==0:
                    return i
                else:
                    continue
            elif i==len(nums)-1:
                if pre1[i-1] == 0:
                    return i
                else:
                    return -1
            else:
                if pre1[i-1] == pre2[i+1]:
                    return i
        return -1