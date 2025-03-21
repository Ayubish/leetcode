# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.childCount = 0
        self.count = 0
    def averageOfSubtree(self, root: TreeNode) -> int:
        def check(root):
            if not root:
                return []
            left = check(root.left)
            right = check(root.right)
           
            prev = [root.val] + left + right
            if root.val == sum(prev)//len(prev):
                self.count += 1
            return prev
        check(root)
        return self.count