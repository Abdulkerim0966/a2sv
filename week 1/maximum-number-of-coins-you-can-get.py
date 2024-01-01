class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        Right=0
        right=1
        ans=0
        left=len(piles)-1
        for i in range(len(piles)//3):
            ans+=piles[right]
            right+=2
        return ans


        