# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans =[]
        def dp(node):
            nonlocal ans
            if not node:
                return
            for i in range(len(node.children)):
                dp(node.children[i])
            ans.append(node.val)
            
        dp(root)
        return ans


        # ans =[]
        # stack = [root]
        # visited=set()
        # while stack:
        #     temp = stack[-1]
            
        #     if not temp:
        #         stack.pop()
        #         continue
        #     if temp in visited:
        #         ans.append(temp.val)
        #         stack.pop()
        #     else:
        #         visited.add(temp)
        #         for i in range(len(temp.children)):
        #             stack.append(temp.children[i])
            
        # return ans



        