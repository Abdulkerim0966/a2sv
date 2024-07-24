# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que =deque([root])
        ans =[root.val]
        while que:
            t =len(que)
            for i in range(t):
                temp =que.popleft()
                if temp.left :
                    que.append(temp.left)
                if temp.right:
                    que.append(temp.right)
            if que:
                ans.append(que[-1].val)
        return ans




        

        

        