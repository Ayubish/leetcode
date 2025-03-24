class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def toTheLeft():
            low = 0
            high  = len(nums) - 1
            start = - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
                    start = mid
            return start
        def toTheRight():
            low = 0
            high  = len(nums) - 1
            end = - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    low = mid + 1
                    end = mid
            return end
        return [toTheLeft(), toTheRight()]