class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left=0
        count=0
        countOdd=0
        for i in range(len(nums)):
            if nums[i]%2==1:
                countOdd+=1
            if countOdd==k:
                temp=0
                while nums[left]%2!=1:
                    left+=1
                    temp+=1
                temp+=1
                left+=1
                right=i+1
                temp2=1
                while right<len(nums) and nums[right]%2!=1:
                    temp2+=1
                    right+=1
                countOdd-=1
                count+=(temp*temp2)
        return count
