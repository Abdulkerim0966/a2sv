# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dect=defaultdict(list)
        lev=0
        def level(node):
            nonlocal lev
            if not node:
                return
            lev+=1
            dect[lev].append(node.val)
            level(node.left)
            level(node.right)
            lev-=1
        level(root)
       

        
        ans=[]
        flag=True
        print(dect)
        for item in sorted(dect):
            if flag:
                flag=False
                ans.append(dect[item])
            else:
                flag=True
                ans.append(dect[item])
                ans[-1].reverse()

        return ans
        
        