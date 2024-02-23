class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        time = tickets[k]
        for i in range(len(tickets)):
            if i<k:
                if tickets[i]>time:
                    ans+=time
                else:
                    ans+=tickets[i]

            elif i == k:
                ans+=time
            else:
                if tickets[i]>(time-1):
                    ans+=(time-1)
                else:
                    ans+=tickets[i]
        return ans

        