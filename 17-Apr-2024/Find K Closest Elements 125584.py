# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans=[]
        idx=bisect_right(arr,x)
        right=idx
        left=idx-1
        n=len(arr)
        for i in range(k):
            
            if left>-1 and (right >= n or (abs(arr[left]-x)<=abs(arr[right]-x))):
                ans.append(arr[left])
                left-=1
            else:
                ans.append(arr[right])
                right+=1
        return sorted(ans)

        