class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        full_set = set()
        for arr in ranges:
            full_set = full_set.union({x for x in range(arr[0], arr[1]+1)})
        sub_set = {x for x in range(left, right+1)}
        return sub_set.issubset(full_set)