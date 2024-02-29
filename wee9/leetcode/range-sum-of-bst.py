# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=0
        def cal(node,l,h):
            nonlocal ans
            if not node :
                return
            if node.val>=l and node.val<=h:
                ans+=node.val
            cal(node.left,l,h)
            cal(node.right,l,h)
        cal(root,low,high)
        return ans
            
        