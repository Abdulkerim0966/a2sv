# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ans =[[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(1,len(ans)):
            for j in range(1,len(ans[0])):
                if s[i-1] == t[j -1]:
                    ans[i][j] = ans[i-1][j-1]+1
                else:
                    ans[i][j] = max(ans[i-1][j],ans[i][j-1])
        # print(ans)
        return ans[len(s)][len(t)] == len(s)
        