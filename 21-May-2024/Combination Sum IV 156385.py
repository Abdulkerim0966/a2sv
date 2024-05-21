# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo ={}
        def dp(n):
            if n ==0:
                return 1
            if n<0:
                return 0
            
            if n not in memo:
                ans =0
                for i in nums:
                    ans+=dp(n-i)
                memo[n] =ans
            return memo[n]
        return dp(target)



        # ans =[[0]*(len(t)+1) for _ in range(len(s)+1)]
        # for i in range(1,len(ans)):
        #     for j in range(1,len(ans[0])):
        #         if s[i-1] == t[j -1]:
        #             ans[i][j] = ans[i-1][j-1]+1
        #         else:
        #             ans[i][j] = max(ans[i-1][j],ans[i][j-1])
        # # print(ans)
        # return ans[len(s)][len(t)] == len(s)

        