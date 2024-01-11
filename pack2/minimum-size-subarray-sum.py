class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        mi=float('inf')
        su=0
        for i in range(len(nums)):
            su+=nums[i]
            # print(su)
            while su>=target:
                # print(su,mi)
                mi=min(mi,i-left+1)
                su-=nums[left]
                left+=1
                # print(mi,left)
        if mi >10000000:
            return 0
        return mi    
            

        