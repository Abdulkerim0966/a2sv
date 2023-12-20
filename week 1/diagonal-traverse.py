class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dect=defaultdict(list)
        ans=[]
        for r in range(len(mat)):
            for c in range (len(mat[0])):
                dect[r+c].append(mat[r][c])
        for item in dect:
            if item %2==0 :
                dect[item].reverse()
                ans.extend(dect[item])
            else:
                ans.extend(dect[item])
        return ans




        