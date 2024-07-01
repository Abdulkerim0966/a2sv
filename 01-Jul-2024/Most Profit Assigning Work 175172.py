# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job = []
        for i in range(len(profit)):
            job.append((difficulty[i] , profit[i]))
        job.sort()
        poi = 0
        ans=0
        worker.sort()
        temp =0
        # print(job)
        for wok in worker:
            while poi <len(job) and wok >= job[poi][0]:
                temp =max(temp,job[poi][1])
                poi+=1
            ans += temp
            # print(ans,wok)
        return ans


        