# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        temp1 =Counter(pattern)
        n =len(temp1)
        ans =[]
        for i in range(len(words)):
            temp =Counter(words[i])
            if n ==len(temp):
                se ={}
                for j in range(len(words[i])):
                    if temp[words[i][j]] != temp1[pattern[j]] or (pattern[j] in se and se[pattern[j]] != words[i][j]):
                        break
                    se[pattern[j]] =words[i][j]
                else:
                    ans.append(words[i])
        return ans

        