class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sumi = sum([k for k in nums if k%2==0])
        for pair in queries:
            if nums[pair[1]]%2 == 0:
                sumi -= nums[pair[1]]                
            nums[pair[1]] += pair[0]
            if nums[pair[1]]%2 == 0:
                sumi += nums[pair[1]]
            ans.append(sumi)
        return ans