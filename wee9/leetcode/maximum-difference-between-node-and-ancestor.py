# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxi=0
        ans=[]
        def caldiff(node):
            nonlocal maxi
            if not node:
                return
            if len(ans):
                maxi=max([abs(max(ans)-node.val),abs(min(ans)-node.val),maxi])
            ans.append(node.val)
            caldiff(node.left)
            caldiff(node.right)
            ans.pop()

            
        caldiff(root)
        return maxi

        



            

            
        