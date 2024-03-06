# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        mini=0
        maxi=n
        while mini<=maxi:
            mid=(maxi+mini)//2
            if guess(mid)==1:
                mini=mid+1
            elif guess(mid)==-1:
                maxi=mid-1
            else:
                return mid
