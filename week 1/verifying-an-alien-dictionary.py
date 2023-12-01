class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ans=True
       
        ord={}
        for i in range (len(order)):
            ord[order[i]]=i+1
        for i in range (len(words)-1):
            for j in range(len(words[i])):
                if j>=len(words[i+1]):
                    ans=False
                    
                    break

                elif ord[words[i][j]]>ord[words[i+1][j]]:
                    ans=False
                    
                    break 
                elif ord[words[i][j]]==ord[words[i+1][j]]:
                    continue
                elif ord[words[i][j]]<ord[words[i+1][j]]:
                    break

                else:
                    continue
            if ans==False:
                break
            
        return ans                 


        