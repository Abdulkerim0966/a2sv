# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo ={}
        def dp(n):
 
            if n == len(questions)-1:
                return questions[n][0]
            
            
            if n not in memo:
                take = questions[n][0] + (dp(n+questions[n][1]+1) if n+1+ questions[n][1] <len(questions) else 0)
                leave = dp(n+1)
                memo[n] = max(leave,take)
            return memo[n]
        
        return dp(0)
        
        