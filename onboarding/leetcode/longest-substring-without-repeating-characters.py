class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_=0
        dect=Counter()
        for i in range (len(s)):
            dect[s[i]]+=1
            while dect[s[i]]>1:
                dect[s[left]]-=1
                left+=1
            max_=max(max_,(i-left+1))
        return max_





        