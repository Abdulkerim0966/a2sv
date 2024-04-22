# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        que =[]
        ans = []
        time = 1
        for i in range (len(tasks)):
            tasks[i].append(i)
        print(tasks)
        heapify(tasks)
        temp =heappop(tasks)
        que.append([temp[1],temp[2],temp[0]])
        heapify(que)
        i = temp[0]
        while que:
            # print(que)
            temp = heappop(que)
            ans.append(temp[1])
            # print(que,'te')
            i += temp[0]
            while tasks and i >= tasks[0][0]:
                temp = heappop(tasks)
                heappush(que,[temp[1],temp[2],temp[0]])

            if not que and tasks:
                temp =heappop(tasks)
                que.append([temp[1],temp[2],temp[0]])
                i = temp[0]

            # print(que,'hehe')
        return ans
            

        