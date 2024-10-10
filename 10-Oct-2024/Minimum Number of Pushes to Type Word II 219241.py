# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        dect= Counter(word)
        ans = 0
        temp =[(dect[key],key) for key in dect]
        temp.sort(reverse=True)
        for i in range(len(temp)):
            ans +=(ceil((i+1)/8)*temp[i][0])
        return ans
        