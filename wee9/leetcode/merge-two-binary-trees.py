# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def marge(node1,node2):
            if not node1 and not node2:
                return 
            if not node1 and node2:
                return node2
            if not node2 and node1:
                return node1

            node=TreeNode( node1.val+node2.val)
            node.left=marge(node1.left,node2.left)
            node.right=marge(node1.right,node2.right)
            return node

        return (marge(root1,root2))

          


        