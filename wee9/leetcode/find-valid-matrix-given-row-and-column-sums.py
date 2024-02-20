class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ans=[]

        for r in range(len(rowSum)):
            temp=[]
            for c in range(len(colSum)):
                p=min(rowSum[r],colSum[c])
                temp.append(p)
                rowSum[r]-=p
                colSum[c]-=p
            ans.append(temp)
        return ans