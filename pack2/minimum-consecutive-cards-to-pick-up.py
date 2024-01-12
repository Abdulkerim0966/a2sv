class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left=0
        dect=set()
        mi=float('inf')
        for i in range(len(cards)):
            if cards[i] in dect:
                while cards[left]!=cards[i]:
                    dect.discard(cards[left])
                    left+=1
                mi=min(mi,(i+1-left))
                left+=1
            else:
                dect.add(cards[i])
        if mi ==float('inf'):
            return -1
        return mi


        