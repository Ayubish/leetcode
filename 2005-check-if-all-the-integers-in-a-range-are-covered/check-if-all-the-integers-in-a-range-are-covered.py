class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        full_set = set()
        for arr in ranges:
            full_set = full_set.union({x for x in range(arr[0], arr[1]+1)})
        for i in range(left, right+1):
            if i not in full_set:
                return False
        return True