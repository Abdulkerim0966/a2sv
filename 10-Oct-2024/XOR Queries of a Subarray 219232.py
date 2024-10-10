# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        for i in range(1,len(arr)):
            arr[i]=arr[i-1]^arr[i]
        ans=[]

        for j in range(len(queries)):
            if queries[j][0] ==0:
                ans.append(arr[queries[j][1]])
            else:
                ans.append(arr[queries[j][1]]^arr[queries[j][0]-1])
        return ans


        