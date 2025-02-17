class NumArray:

    def __init__(self, nums: List[int]):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)
        self.prefix_sum = prefix_sum
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)