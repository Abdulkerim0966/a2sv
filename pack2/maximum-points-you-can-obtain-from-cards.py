class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        su=sum(cardPoints[0:k])
        right=len(cardPoints)-1
        n=k-1
        ma=su
        for i in range(k):
            su-=cardPoints[n]
            su+=cardPoints[right]
            n-=1
            right-=1
            ma=max(ma,su)
        return ma
            



