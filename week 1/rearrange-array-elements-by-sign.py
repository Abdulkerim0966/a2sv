class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[]
        pos=[]
        ne=[]
        for i in range(len(nums)):
            if nums[i]<=0:
                ne.append(nums[i])
            else:
                pos.append(nums[i])
        for i in range(len(nums)//2):
            ans.append(pos[i])
            ans.append(ne[i])
        return ans
        