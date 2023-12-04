class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ma=0
        ans=""
        for i in range (len(num)-2):
            if num[i]==num[i+1] ==num[i+2]:
                if ma<=int(num[i:i+3]):
                    ma=int(num[i:i+3])
                    ans=num[i:i+3]
            
        return ans