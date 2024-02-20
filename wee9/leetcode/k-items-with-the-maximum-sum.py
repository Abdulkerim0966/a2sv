class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans=0
        if k<=numOnes:
            ans+=k
        elif k<=(numOnes+numZeros):
            ans=numOnes
        else:
            n=k-(numOnes+numZeros)
            ans=(numOnes-n)
        return ans
        