# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, left, right):
        if not (left or right):
            return True
        if not right:
            return False
        if not left:
            return False
        return left.val == right.val and (self.check(left.left, right.right) and self.check(left.right, right.left))
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root.left, root.right)