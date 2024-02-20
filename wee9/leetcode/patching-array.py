class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr=0
        count=0
        for i in range(len(nums)):
            if curr>=n:
                return count
            while curr<nums[i]-1:
                if curr>=n:
                    break
                curr+=(curr+1)
                count+=1
            curr+=nums[i]
        while curr<n:
            curr+=(curr+1)
            count+=1
        return count

