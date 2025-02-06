class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dicto = Counter(nums)
        ans = []
        n = len(nums)//3
        for num in dicto:
            if dicto[num]>n:
                ans.append(num)
        return ans