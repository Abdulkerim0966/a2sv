class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        ans=0
        dect=Counter()
        for i in range(len(answers)):
            
            if dect[answers[i]]==0:
                dect[answers[i]]=answers[i]
                ans+=(answers[i]+1)
            else:
                dect[answers[i]]-=1
        return ans


        