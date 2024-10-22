# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dp(node):
            if not node:
                return [True,0]
            l= [True,0]
            if node.left:
                temp =dp(node.left)
                l[0] =temp[0]
                l[1] =temp[1] 
            
            r= [True,0]
            if node.right:
                temp =dp(node.right)
                r[0] =temp[0]
                r[1] =temp[1] 
            if l[0] and r[0] and (abs(l[1]-r[1]) <=1):
                return [True,max(l[1] ,r[1])+1]
            else:
                return[False,max(l[1] ,r[1])+1]
            

        

        return dp(root)[0]
    
        