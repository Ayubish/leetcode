class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        low = 1
        high = max(ranks)*cars**2
        def isvalid(mid):
            count = 0

            for rank in ranks:
                l = mid//rank
                l = math.floor(l**0.5)
                count += l
            return count >= cars
        
        while low <= high:
            mid = low + (high-low)//2

            if isvalid(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low