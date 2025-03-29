class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        def isvalid(mid):

            count = 0
            for candy in candies:
                count += (candy//mid)
            return count >= k

        low = 1
        high = max(candies)

        while low <= high:
            mid = low + (high-low)//2
            if isvalid(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high
    