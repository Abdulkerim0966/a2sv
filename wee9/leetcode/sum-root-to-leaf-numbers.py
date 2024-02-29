# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0
        ans2=0
        def sumr(node):
            nonlocal ans
            nonlocal ans2
            if not node:
                return
            
            ans=ans*10+node.val
            sumr(node.left)
            sumr(node.right)
            if not node.right and not node.left:
                ans2+=ans
            ans//=10
        sumr(root)
        
        return ans2








