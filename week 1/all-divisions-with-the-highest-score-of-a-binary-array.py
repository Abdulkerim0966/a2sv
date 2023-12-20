class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        dect=defaultdict(list)
        no_ones=nums.count(1)
        no_zero=0
        for i in range(len(nums)):
            dect[no_ones+no_zero].append(i)
            if nums[i]==0:
                no_zero+=1
            else:
                no_ones-=1
            if i==len(nums)-1:
                dect[no_ones+no_zero].append(i+1)

        ma =max(dect.keys())
       
        return dect[ma]
        