class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ma=(s[0:k].count('a')+s[0:k].count('e')+s[0:k].count('i')+s[0:k].count('o')+s[0:k].count('u'))
        left=0
        count=ma
        for i in range(k,len(s)):
            if s[left]=='a' or s[left]=='e' or s[left]=='i' or s[left]=='o' or s[left]=='u':
                count-=1
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
                count+=1
            left+=1
            ma=max(ma,count)
        return ma

        