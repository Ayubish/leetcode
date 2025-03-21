# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root):
            if not root:
                return []
            val = [root.val]
            left = inorder(root.left)
            right = inorder(root.right)
            
            return left + val + right
            
        nums = inorder(root)

        def assemble(nums):
            if not nums:
                return
            mid = len(nums)//2
            parent = TreeNode(nums[mid])
            parent.left = assemble(nums[:mid])
            parent.right = assemble(nums[mid+1:])

            return parent
        return assemble(nums)
            