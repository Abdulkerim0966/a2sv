# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        score = [[0]*26 for i in range(len(words))]
        ma =0
        for i in range(len(words)):
            for j in range(len(words[i])):
                score[i][ord(words[i][j])-97] =1
        for i in range(len(score)-1):
            for j in range(i+1,len(score)):
                fl =True
                for k in range(26):
                    if score[i][k] == score[j][k] and score[i][k] == 1:
                        fl =False
                        break
                if fl:
                    ma =max(ma,(len(words[i])*len(words[j])))
        
        return ma