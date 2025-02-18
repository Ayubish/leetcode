class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix=[0]
        for num in nums:
            if num == 0:
                prefix.append(prefix[-1]-1)
            else:
                prefix.append(prefix[-1]+1)
        maxi = 0
        dicto = {}
        for i in range(len(prefix)):
            if prefix[i] not in dicto:
                dicto[prefix[i]] = i
            else:
                if i - dicto[prefix[i]] > maxi:
                    maxi = i - dicto[prefix[i]]
        return maxi
