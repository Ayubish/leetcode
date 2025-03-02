class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        extra = k
        l, r, = 0, 0
        maxi = 0
        temp = 0
        while r<len(nums):
            if nums[r] == 1:
                temp += 1
                r += 1
            elif extra>0:
                temp += 1
                extra -= 1
                r += 1
            else:
                maxi = max(maxi, temp)
                if nums[l] == 0:
                    extra += 1
                l += 1
                temp -= 1
        maxi = max(maxi, temp)
        return maxi
        