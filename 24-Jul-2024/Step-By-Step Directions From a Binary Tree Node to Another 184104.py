# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        s = []
        e=[]
        temp =[]
        def dfs(node,w):
            temp.append([node.val,w])

            if node.val == startValue:
                s.extend(temp)
            if node.val == destValue:
                e.extend(temp) 

            if node.left:
                dfs(node.left,'L')
            if node.right:
                dfs(node.right,'R')
            temp.pop()
        dfs(root,'f')

        ans =[]
        i =0
        while i<len(s) and i<len(e) and s[i]==e[i]:
            i+=1
        temp =["U"]*(len(s)-i)
        while i < len(e):
            temp.append(e[i][1])
            i+=1

        return ''.join(temp)
        



        