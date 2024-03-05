class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        bucket=[]
        ans=[]
      
        def backtrack(idx):

            if len(bucket)==k:
                ans.append(bucket[:])
                return 
            

            for i in range(idx+1,n+1):
               
                bucket.append(i)
                backtrack(i)
                bucket.pop()
        backtrack(0)
        return ans
       