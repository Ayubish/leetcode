class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dicto = Counter(nums)
        ans = [item for item in dicto if dicto[item] == 2]
        return ans