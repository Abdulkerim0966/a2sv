class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range (len(matrix[0])):
            temp=[]
            for c in range (len(matrix)):
                temp.append(matrix[c][i])
            ans.append(temp)
        return ans
        