class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        count = 0
        ans = []
        for key, val in d.items():
            if count>=2:
                break
            if val==2:
                ans.append(key)
                count+=1
        return ans

            