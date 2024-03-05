# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        def trave(node,r,c):

            if not node:
                return
            
            trave(node.left,r-1,c+1)
            ans.append((r,c,node.val))
            trave(node.right,r+1,c+1)


        trave(root,0,0)
        ans.sort()
        ans2=[]
        i=0
        while i<len(ans):
            temp=[]
            temp.append(ans[i][2])
            i+=1
            while i<len(ans)  and ans[i][0]==ans[i-1][0]:
                temp.append(ans[i][2])
                i+=1
            ans2.append(temp)
        print (ans,ans2)

        return ans2