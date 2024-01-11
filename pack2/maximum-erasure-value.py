class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left=0
        uni=set()
        ma=0
        su=0
        for i in range(len(nums)):
            if nums[i] not in uni:
                su+=nums[i]
                uni.add(nums[i])
                ma=max(ma,su)
            else:
                print(left,ma,i)
                while nums[left]!=nums[i]:
                    su-=nums[left]
                    uni.discard(nums[left])
                    left+=1
                left+=1
                ma=max(ma,su)
                print(left,ma,i)

        return ma
        