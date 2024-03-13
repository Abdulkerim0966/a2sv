class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count=0
        ma=nums[-1]
        for i in range(len(nums)-1,-1,-1):
              
            temp2=count
            count+=(((nums[i]+(ma-1))//ma)-1)
               
              
            ma=nums[i]//((count+1)-temp2)
            print(ma)
        return count
        # operations = 0
        # prev_bound = nums[-1]

        # for num in reversed(nums[:-1]):
        #     no_of_times = (num + prev_bound - 1) // prev_bound
        #     operations += no_of_times - 1
        #     prev_bound = num // no_of_times
            
        # return operations