class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
       
        ans=[nums[i] for i in range(1,len(nums),+2) for j in range(0,nums[i-1])]
    
        return ans


        