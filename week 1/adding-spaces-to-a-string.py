class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        space=set(spaces)
        ans=""
        for i  in range(len(s)):
            if i in space:
                ans+=" "
                ans+=s[i]
            else:
                ans+=s[i]
        return ans

    
        