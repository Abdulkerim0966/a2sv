class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        bucket=[]
        ans=set()
        candidates.sort()
        poped=[]
        n=len(candidates)
        def backtrack(idx):
            
            if sum(bucket)==target:
                ans.add(tuple(bucket.copy()))
                return 

            if sum(bucket)>target: 
                return 

            for i in range(idx,n):
                if poped and candidates[i]==poped[-1]:  
                    continue              
                bucket.append(candidates[i])
                backtrack(i+1)
                poped.append(bucket[-1])
                bucket.pop()
                
        backtrack(0)

        return [list(a) for a in ans]
        