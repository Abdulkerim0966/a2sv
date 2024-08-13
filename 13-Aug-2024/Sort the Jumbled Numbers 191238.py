# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        dect ={}
        for i in range(len(mapping)):
            dect[str(i)] =str(mapping[i])
        def co(num):
            s=list(str(num))
            for i in range(len(s)):
                s[i] =dect[s[i]]
            return int(''.join(s))
        nums.sort(key=lambda x:co(x))
        return nums

