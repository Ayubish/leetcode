class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s = ''.join([str(k) for k in nums])
        return [int(k) for k in s]