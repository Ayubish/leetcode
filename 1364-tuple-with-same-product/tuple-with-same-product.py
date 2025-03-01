class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dicto = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                dicto[nums[i]*nums[j]] += 1
        result = 0
        print(dicto)
        for val in dicto.values():
            result += (val*(val-1))//2
        return result*8