class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        pointer=0
        pointer2=0
        fl=False
        count=0
        ans=[]
        ans.append(0)
        if 0 not in nums:
            return len(nums)-1
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            elif fl==False:
                fl=True
                pointer=count
            else:
                ans.append(count-pointer2)
                pointer2=pointer
                pointer=count
        print(count,pointer2)        
        ans.append((count)-pointer2)
        return max(ans)
        