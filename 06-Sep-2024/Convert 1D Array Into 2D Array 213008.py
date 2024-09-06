# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        i =0
        ans = []
        for r in range(m):
            temp =[]
            for c in range(n):
                temp.append(original[i])
                i+=1
            ans.append(temp.copy())
        return ans
            
        