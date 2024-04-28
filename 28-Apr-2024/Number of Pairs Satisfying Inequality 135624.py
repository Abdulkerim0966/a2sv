# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        for i in range(n):
            nums1[i] -= nums2[i]
        
        def getCounts(left, right):
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            leftCount = getCounts(left, mid)
            rightCount = getCounts(mid + 1, right)

            count = 0
            copy = nums1[left:mid+1]
            copy.sort()

            for i in range(mid + 1, right + 1):
                count += bisect_right(copy, nums1[i] + diff)

            return leftCount + rightCount + count

        return getCounts(0, n - 1)