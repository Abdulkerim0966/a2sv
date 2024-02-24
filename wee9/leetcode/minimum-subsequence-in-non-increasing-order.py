class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total=sum(nums)
        nums.sort(reverse=True)
        count=0
        i=0
        ans=[]
        while count<=(total-count):
            count+=nums[i]
            ans.append(nums[i])
            i+=1
        return ans
        

        