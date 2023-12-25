class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        al=set(allowed)
        count=0
        for i in range(len(words)):
            f1=True
            for j in range(len(words[i])):
                if words[i][j] not in al:
                    f1=False

            if f1==True:
                count+=1
        return count

        