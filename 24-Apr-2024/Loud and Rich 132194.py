# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        dect = defaultdict(list)
        outgo = defaultdict(int)
        ans = [i for i in range(len(quiet))]

        for rich , poor in richer:
            dect[rich].append(poor)
            outgo[poor]+=1


        que =deque()
        for ind in dect :
            if outgo[ind] == 0:
                que.append(ind)
    
        while que:
            temp = que.popleft()
           
            for nigh in dect[temp]:
                outgo[nigh ] -= 1
                # print(quiet[ans[temp]],temp,quiet[nigh],nigh)
                if quiet[ans[temp]] <= quiet[ans[nigh]]:
                    ans[nigh]  = ans[temp]

                if outgo[nigh ] == 0:
                    que.append(nigh)
            # print(ans)
        return ans



        
        