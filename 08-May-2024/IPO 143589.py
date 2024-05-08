# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        temp =[]
        temp1 =[]
        for i in range(len(capital)):
            temp1.append((capital[i],profits[i]))
        temp1.sort()
        poi =0
        while k > 0:

            while poi <len(temp1) and temp1[poi][0] <= w:
                heappush(temp,(-temp1[poi][1],temp1[poi][0]))
                poi+=1
            if temp:
                now =heappop(temp)
                w -=now[0]
            k-=1
        return w
            
        