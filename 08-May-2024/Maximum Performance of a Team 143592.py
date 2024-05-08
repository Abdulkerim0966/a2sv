# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        score =[(efficiency[i],speed[i]) for i in range(len(speed))]
        score.sort(reverse =True)
        summ =0
        hea =[]
        ma =0
        for i in range(len(score)):
            if len(hea) ==k:
                summ-=heappop(hea)[0]
                summ +=score[i][1]
                ma=max(ma,(score[i][0]*summ))
                heappush(hea,(score[i][1],score[i][0]))
            else:
                summ +=score[i][1]
                ma=max(ma,(score[i][0]*summ))
                heappush(hea,(score[i][1],score[i][0]))
        return ma%(10**9 +7)




