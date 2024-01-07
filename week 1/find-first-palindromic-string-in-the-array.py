class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            right=len(words[i])-1
            left=0
            f1=False
            while left<right:
                if words[i][left]!=words[i][right]:
                    f1=True 
                    break
                else:
                    right-=1
                    left+=1
            if f1==False:
                return words[i]
        return ("")
        