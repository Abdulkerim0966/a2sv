# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dect=defaultdict(int)
        count=0
        for i in range (len(arr)):
            temp=k-(arr[i]%k)
            if arr[i]%k ==0:
                count+=1

            elif dect[temp]>0:
                dect[temp]-=1
  
            else : 
                dect[arr[i]%k]+=1
       
        for i in dect:
            if dect[i] > 0:
                return False
        return count%2 == 0
        


        