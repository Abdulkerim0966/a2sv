# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def post(node):
            if node:
                post(node.left)
                post(node.right)
                ans.append(node.val)
            else:
                return
        post(root)
        return ans