class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        se=set(s[i] for i in range(len(s)) )
        left=0
        ma=0
        count=0
        for ch in se:
            for i in range(len(s)):
                if s[i]!=ch:
                    count+=1
                while count>k:
                    if s[left]!=ch:
                        count-=1
                    left+=1
                ma=max(ma,i-left+1)
            count=0
            left=0
        return ma




        