class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        bucket=[]
        ans=[]
        n = len(nums)
        def backtrack():

            if len(bucket)==n:
                ans.append(bucket[:])
                return 
            

            for i in range(n):
                if nums[i] in bucket:
                    continue
                bucket.append(nums[i])
                backtrack()
                bucket.pop()
        backtrack()
        return ans
        