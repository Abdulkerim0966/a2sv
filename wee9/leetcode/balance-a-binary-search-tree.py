# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ans=[]
        def traverse(node):
            if not node:
                return

            ans.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        ans.sort()
        def sortedArrayToBST(arr: List[int]) -> Optional[TreeNode]:
            if not arr:
                return
            mid=(len(arr))//2
            root=TreeNode()
            root.val=arr[mid]

            root.left=sortedArrayToBST(arr[:mid])
            root.right=sortedArrayToBST(arr[mid+1:])

            return root
        return sortedArrayToBST(ans)
       
            

        