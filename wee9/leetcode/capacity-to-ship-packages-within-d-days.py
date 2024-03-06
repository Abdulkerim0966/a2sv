class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        maxi=sum(weights)
        mini=max(weights)
       
        def cal(mid):
            count=1
            load=0
            for i in range(len(weights)):
                load+=weights[i]
                if load>mid:
                    count+=1
                    load=weights[i]
                
                if count>days:
                    return False
            return True

        while mini<maxi:
            mid=(mini+maxi)//2
            flag=cal(mid)
            if flag:
                maxi=mid
            elif not flag:
                mini=mid+1
            
        return maxi















        