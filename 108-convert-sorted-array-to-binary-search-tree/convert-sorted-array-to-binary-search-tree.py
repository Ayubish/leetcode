# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # mid = len(nums)//2
        # root = TreeNode(nums[mid])
        def assembler(qurach):
            if not qurach:
                return
            mid = len(qurach)//2
            root = TreeNode(qurach[mid])

            root.left = assembler(qurach[:mid])
            root.right = assembler(qurach[mid+1:])
            return root
        return assembler(nums)