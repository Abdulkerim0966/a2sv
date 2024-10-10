# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays.sort()
      
        mi =arrays[0][0]
        ma =arrays[0][-1]
        ans =0
        for i in range(1,len(arrays)):
            temp = max(abs(mi -arrays[i][-1]),abs(ma-arrays[i][0]))
            ans=max(ans,temp)
            mi=min(mi,arrays[i][0])
            ma = max(ma,arrays[i][-1])
        return ans
