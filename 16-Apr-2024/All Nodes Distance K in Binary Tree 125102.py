# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        dect  = defaultdict(list)
       
        def dfs(root):
            if not root:
                return
            
            if root.left:
                dect[root.val].append(root.left.val)
                dect[root.left.val].append(root.val)
                dfs(root.left)

            if root.right:
                dect[root.val].append(root.right.val)
                dect[root.right.val].append(root.val)
                dfs(root.right)

        dfs(root)

        print(dect)
        que = deque() 
        visited= set()

        que.append(target.val)
        visited.add(target.val)
        
        count =0
        while que and count < k:

            for i in range(len(que)):
                temp = que.popleft()
               
                for nigh in dect[temp]:
                  
                    if nigh not in visited:
                        que.append(nigh)
                        visited.add(nigh)
            
            count +=1
       
        return list(que)

       
       




