class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans=[0]*(max(costs)+1)
        per=0
        for i in range(len(costs)):
            ans[costs[i]]+=1
        for i in range (len(ans)):
            no=ans[i]
            while no>0:
                if coins>=i:
                    coins-=i
                    per+=1
                    no-=1
                else:
                    break

        return per
                


        