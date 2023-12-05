class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ma=max(candies)
        ans=[]
        for i in range(len(candies)):
            if ma<=(candies[i]+extraCandies):
                ans.append(True)
            else:
                ans.append(False)
        return ans
        