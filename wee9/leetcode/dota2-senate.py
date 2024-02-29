class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dect=Counter(senate)
        que=deque(senate)
        band=0
        banr=0
        while que:
            if que[0]=='R':
                if banr==0:
                    band+=1
                    dect['D']-=1

                    que.append(que.popleft())
                else:
                    banr-=1
                    que.popleft()
                 
                if dect['D']<=0 or len(que)==1:
                    return "Radiant"
            else:
                if band==0:
                    banr+=1
                    dect['R']-=1

                    que.append(que.popleft())
            
                else:
                    band-=1
                    que.popleft()
                if dect['R']<=0 or len(que)==1:
                    return "Dire"
            
        