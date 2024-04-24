# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans =[set() for i in range(n)]
        dect =defaultdict(list)
        outgo = defaultdict(int)

        for item ,to in edges:
            dect[item].append(to)
            outgo [to] +=1
        que = deque()
        for i in range(n):
            if outgo[i] ==0:
                que.append(i)
        
        while que:
            temp =que.popleft()
            for nigh in dect[temp]:
                outgo[nigh] -= 1
                ans[nigh].add(temp)
                ans[nigh].update(ans[temp])
                if outgo[nigh] == 0:
                    que.append(nigh)
        ans2=[]       
        for item in ans:
            ans2.append(list(item))
        for item in ans2:  
            item.sort()
        return ans2
        