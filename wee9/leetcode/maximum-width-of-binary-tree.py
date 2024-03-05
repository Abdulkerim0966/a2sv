# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=[]
        def trave(node,i,flag):

            if not node:
                return
            
            trave(node.left,i+1,2*flag)
            ans.append((i,flag))
            trave(node.right,i+1,2*flag+1)

        trave(root,0,0)
        ans.sort()
        print(ans)
        maxi=1
        i=0
        while i<len(ans):
            inil=ans[i][0]
            ini=ans[i][1]
            while i<len(ans) and inil==ans[i][0]:
                i+=1
            i-=1
            maxi=max(maxi,((ans[i][1]-ini)+1))
            i+=1

        return maxi
        