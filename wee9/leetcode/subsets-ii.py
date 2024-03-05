class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        current=[]
        ans=set()

        def backtrack(idx):

            ans.add(tuple(sorted(current.copy()))) 
            

            for i in range(idx,len(nums)):
               
                current.append(nums[i])
                backtrack(i+1)
                
                current.pop()
            return ans
        ans=backtrack(0)

        return [list(a) for a in ans]