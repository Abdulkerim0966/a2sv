# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph =defaultdict(list)
        temp =[]
        def cons(node):
            nonlocal graph
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                cons(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                cons(node.right)
            if not node.left and not node.right :
                temp.append(node)
        
        cons(root)
  
        ans =0
        
        def dfs(node,le,visited):
            nonlocal ans
            visited.add(node)
            if le > distance:
                return 
            if len(graph[node]) ==1 and le != 0 and node != root:
                ans+=1
                return
            for nigh in graph[node]:
                if nigh not in visited:
                    dfs(nigh,le+1,visited.copy()) 
        for node in temp: 
            dfs(node,0,set())
        return ans//2
            

       


        