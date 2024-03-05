class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        bucket=[]
        ans=set()
        
        def backtrack(idx):
            
            if sum(bucket)==n and len(bucket)==k:
                ans.add(tuple(bucket.copy()))
                return 
       
            if sum(bucket)>n or len(bucket)>k: 
                return 

            for i in range(idx,10):
                         
                bucket.append(i)
                backtrack(i+1)
                bucket.pop()
                
        backtrack(1)

        return [list(a) for a in ans]