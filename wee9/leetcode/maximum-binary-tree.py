# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return

        maxi=max(nums)
        ma=nums.index(maxi)

        node=TreeNode()
        node.val=maxi
        node.left=self.constructMaximumBinaryTree(nums[:ma])
        node.right=self.constructMaximumBinaryTree(nums[ma+1:])
        return node


        