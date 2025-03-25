class Solution(object):
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)
        def counter(m):
            d = 1
            currSum = 0
            for num in weights:
                if currSum+num>mid:
                    d += 1
                    currSum = num
                else:
                    currSum += num
            return d
        while left< right:
            mid = left+(right-left)//2
            if counter(mid)<=days:
                right = mid
            else:
                left = mid+1
        return left
        