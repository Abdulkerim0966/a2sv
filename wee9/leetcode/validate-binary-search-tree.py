# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[]
        def valid(node):
            if not node:
                return
            valid(node.left)
            ans.append(node.val)
            valid(node.right)
        valid(root)
        for i in range(1,len(ans)):
            if ans[i]<=ans[i-1] :
                return False
                    
        
        return True
        