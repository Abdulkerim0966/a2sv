class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        left=0
        right=left+1
        ans=[]
        while right<len(nums) :
            a=[nums[right]]
            b=a*nums[left]
            ans.extend(b)
            left+=2
            right+=2
        return ans


        