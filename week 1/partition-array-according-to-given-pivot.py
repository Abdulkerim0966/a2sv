class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        great=[]
        equal=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                less.append(nums[i])
            elif nums[i]>pivot:
                great.append(nums[i])
            else:
                equal.append(nums[i])
        ans=less+equal+great
        return ans

        