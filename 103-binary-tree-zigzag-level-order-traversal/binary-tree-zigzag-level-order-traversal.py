# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        zigzag_dict = defaultdict(list)
        def zigzag(root, index):
            if not root:
                return 
            zigzag_dict[index].append(root.val)
            zigzag(root.left, index+1)
            zigzag(root.right, index+1)
        zigzag(root, 0)
        ans = list(zigzag_dict.values())
        for i in range(len(ans)):
            if i%2:
                ans[i].reverse()
        return ans