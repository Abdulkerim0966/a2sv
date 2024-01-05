class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: 

        if sum(gas)>=sum(cost):
            sum_=0
            pointer=0
            for i in range(len(gas)):
                sum_+=gas[i]-cost[i]
                if sum_<0:
                    sum_=0
                    pointer=i+1
            return pointer
             
        else:
            return -1
        