# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global dep
        global ma
        dep=0
        ma=0
        def find(node):
            global dep
            global ma
            if not node:
                ma=max(ma,dep)
                return
            dep+=1
            find(node.left)
            find(node.right)
            dep-=1
        find(root)
        return ma
        