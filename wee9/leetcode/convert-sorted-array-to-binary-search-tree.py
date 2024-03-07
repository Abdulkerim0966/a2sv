# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, arr: List[int]) -> Optional[TreeNode]:
        if not arr:
            return
        mid=(len(arr))//2
        root=TreeNode()
        root.val=arr[mid]

        root.left=self.sortedArrayToBST(arr[:mid])
        root.right=self.sortedArrayToBST(arr[mid+1:])

        return root



        

        
        
        

