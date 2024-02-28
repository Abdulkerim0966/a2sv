# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dect=Counter()
        def calculator(node):
            if not node:
                return
            calculator(node.left)
            calculator(node.right)
            dect[node.val]+=1
        calculator(root)
        max_ = max(dect.values())
        return [key for key in dect if dect[key] == max_]
            
            