class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans=deque()
        deck.sort(reverse=True)
        ans.append(deck[0])
        for i in range(1,len(deck)):
            ans.appendleft(ans.pop())
            ans.appendleft(deck[i])
        return ans
        