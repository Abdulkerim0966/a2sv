# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dect = defaultdict(list)
        outgo = defaultdict(int)
        safe =set()
        visited =set()
        ans = []
        def dfs(node):
            # print(node)
            if node in visited and node  not in safe :
                return False
            if node in visited and node in safe :
                return True

            temp = True
            visited.add(node)
            for nigh in graph[node]:
                temp = temp and dfs(nigh)

            if temp:
                safe.add(node)
                return True
   
        for i in range(len(graph)):

            if i not in visited:
                dfs(i)
             

        return sorted(safe)

        





        
        