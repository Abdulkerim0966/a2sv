# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] =(-nums[i])
        heapify(nums)
        ans =0
        for i in range(k):
            temp =heappop(nums)
            ans-=temp
            temp = ceil((-temp)/3)
            heappush(nums,-temp)
        return ans