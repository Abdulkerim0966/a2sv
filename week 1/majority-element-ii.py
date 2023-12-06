class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            if nums.count(nums[i])>(len(nums)/3):
                if nums[i] not in ans:
                    ans.append(nums[i])
        return ans
        