# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def bellman_ford(n, edges, src):
            nonlocal k
            distpre = [float('inf')] * n
            distcur =[float('inf')] * n
            distpre[src] = 0
            distcur[src] = 0
            for i in range(k+1):
                # print(i)
                any_relaxation = False
            
                for u, v, w in edges:
                    
                    if distpre[u] != float('inf') and distpre[u] + w < distcur[v]:
                        # print("heere",u,v,w,distpre[u],distpre[v])
                        distcur[v] = distpre[u] + w
                        any_relaxation = True
                distpre = distcur[:]
                # print(i,distcur)
                if not any_relaxation:
                    break
            return distcur
        d =bellman_ford(n, flights, src)
        # print(d)
        return d[dst] if d[dst]!=float("inf") else -1