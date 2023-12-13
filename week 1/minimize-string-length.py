class Solution:
    def minimizedStringLength(self, s: str) -> int:
        ans=set()
        for i in range(len(s)):
            ans.add(s[i])

        return len(ans)

        