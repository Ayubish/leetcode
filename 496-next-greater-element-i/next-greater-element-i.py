class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono_stack  = [nums2[0]]
        dic = {}
        for i in range(1, len(nums2)):
            while mono_stack and nums2[i]>mono_stack[-1]:
                dic[mono_stack[-1]] = nums2[i]
                mono_stack.pop()
            mono_stack.append(nums2[i])
        ans = []
        for num in nums1:
            if num in dic:
                ans.append(dic[num])
            else:
                ans.append(-1)
        return ans
            