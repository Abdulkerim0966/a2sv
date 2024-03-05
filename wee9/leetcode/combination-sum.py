class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        bucket=[]
        ans=[]
   
        n=len(candidates)
        def backtrack(idx):
            
            if sum(bucket)==target:
                ans.append(bucket.copy())
                return 

            if sum(bucket)>target: 
                return 

            for i in range(idx,n):
                bucket.append(candidates[i])
                backtrack(i)
                bucket.pop()
        backtrack(0)


        return ans