# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1]*n
        ans[0] = 0
        que = deque()
        dectr = defaultdict(list)
        dectb = defaultdict(list)
        for r ,c in redEdges:
            dectr[r].append(c)
        for r ,c in blueEdges:
            dectb[r].append(c)

        que.extend(dectr[0])

        tru = True
        count = 0

        visitedb =defaultdict(int)
        visitedr=defaultdict(int)
        visitedr[0] += 1
        # print(dectr,dectb)
        while que :
            count+=1
            n = len(que)
            # print(que)
            for i in range(n):
                temp = que.popleft()
                # print(temp,tru)
                if ans[temp] == -1 or ans[temp] > count :
                    ans[temp] = count
                if tru:
                    if temp in dectb and visitedb[temp]<2:
                        visitedb[temp] +=1
                        que.extend(dectb[temp])
                        
                else:
                    if temp in dectr and visitedr[temp]<2:
                        visitedr[temp] +=1
                        que.extend(dectr[temp])
            tru = not tru
                        

   
        que.extend(dectb[0])
        tru = False
        count = 0
        visitedb =defaultdict(int)
        visitedr=defaultdict(int)
        visitedb[0]+=1
       
        while que :
            count+=1
            n = len(que)
            for i in range(n):
                temp = que.popleft()
                if ans[temp] == -1 or ans[temp] > count :
                    ans[temp] = count
                if tru:
                    if temp in dectb and visitedb[temp]<2:
                        visitedb[temp] +=1
                        que.extend(dectb[temp])
                       
                else:
                    if temp in dectr and visitedr[temp]<2:
                        visitedr[temp] +=1
                        que.extend(dectr[temp])
            tru = not tru
                      
        return ans

                    







        