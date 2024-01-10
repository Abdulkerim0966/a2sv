class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left=0
        count=0
        ma=0
        for i in range(len(answerKey)):
            if answerKey[i]=='T':
                count+=1
            while count>k:
                if answerKey[left]=='T':
                    count-=1
                left+=1
            ma=max(ma,i-left+1)
        left=0
        count=0
        
        for i in range(len(answerKey)):
            if answerKey[i]=='F':
                count+=1
            while count>k:
                if answerKey[left]=='F':
                    count-=1
                left+=1
            ma=max(ma,i-left+1)
            # print(ma,i-left+1,i,left)
        return ma
        