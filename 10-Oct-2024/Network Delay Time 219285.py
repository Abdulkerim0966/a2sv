# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph =defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
            
        def dijkstra(graph, start_node):
            distances = {node: float('inf') for node in graph}
            distances[start_node] = 0
            processed = set()
            heap = [(0, start_node)]
            while heap:
                temp =heappop(heap)
                if temp[1] not in processed:
                    processed.add(temp[1])
                    distances[temp[1]] =temp[0]
                    for nign in graph[temp[1]]:                   
                        heappush(heap,(nign[1]+temp[0],nign[0]))       
                # Write your code here
            print(distances)
            return distances
        d =dijkstra(graph, k)
        ma=-1
        i =0
        for key in d:
            i+=1
            ma =max(ma,d[key])
        if i <n:
            return -1
        return ma if ma !=float("inf") else -1
        