class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dect={}
        ans=""
        for ind,va in enumerate(indices):
            dect[va]=ind
        for i in range(len(s)):
            ans += s[dect[i]]
        return ans
        
