class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def checker(mid):
            count=0
            for i in range(len(nums)):
                count+=(ceil(nums[i]/mid))
                if count>threshold:
                    return False
            return True

        mini=1
        maxi=max(nums) 
        
        while mini<=maxi:
            mid=(maxi+mini)//2
            if checker(mid):
                maxi=mid-1
            else:
                mini=mid+1
        return mini

        