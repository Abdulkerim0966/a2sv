# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo ={}
        def dp(n):
            
            if n>=len(days):
                return 0
            if n not in memo:
                mi = float('inf')
                for i in range(len(costs)):
                    if i == 0:
                        mi =min(mi, costs[i]+ dp(n+1))
                    elif i == 1:
                        t =days[n]+7
                        p =n
                        while p<len(days) and days[p] <t:
                            p +=1
                        mi = min(mi,costs[i]+dp(p))
                    else:
                        t = days[n]+30
                        q =n
                        while q<len(days) and days[q] <t:
                            q +=1
                        mi = min(mi,costs[i]+dp(q))
                memo[n] = mi
            return memo[n]
        return dp(0)





        