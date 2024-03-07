class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        count=0
        print (nums)
        for i in range(len(nums)):
            x=target-nums[i]
        
            idx=bisect_right(nums,x)
            if idx>i:
                
                count+=(2**((idx-i)-1))
            
    
        return (count%((10**9) + 7))