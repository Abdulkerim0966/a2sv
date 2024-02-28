# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans=[]
        def cal(node,flag):
            if not node:
                return
            cal(node.left,True)
            ans.append((node.val,flag))
            cal(node.right,False)
        cal(p,True)
        ans1=ans.copy()
        ans.clear()
        cal(q,True)
        print(ans1,ans)
        return ans==ans1 
        
