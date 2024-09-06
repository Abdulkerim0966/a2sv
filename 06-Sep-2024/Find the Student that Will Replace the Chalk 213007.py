# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        su =sum(chalk)
        curr =k%su
        for i in range(len(chalk)):
            curr -=chalk[i]
            if curr<0:
                return i
        return len(chalk)-1
        