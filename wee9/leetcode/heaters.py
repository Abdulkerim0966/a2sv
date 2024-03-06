class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def checker(ra):
            j=0
            for i in range(len(houses)):

                flag=False
                while j<len(heaters):
  
                   
                    if abs(houses[i]-heaters[j])<=ra:
                       
                        flag=True
                        break
                    if houses[i]-heaters[j]<(-ra):
                        return False
                    j+=1
              
                if not flag and abs(houses[i]-heaters[-1])>ra:
                    return False

            return True
        
        maxi=max(max(houses),max(heaters))
        mini=0
        
        while mini<=maxi:
            mid=(mini+maxi)//2
            temp=checker(mid)
            print(mid,temp)
            
            if temp:
                maxi=mid-1
            else:
                mini=mid+1
        return mini













