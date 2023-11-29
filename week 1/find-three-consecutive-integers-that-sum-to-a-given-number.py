class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        re=[]
        a=(num//3)-1
        if (a+(a+1)+(a+2))==num:
            re.append(a)
            re.append(a+1)
            re.append(a+2)
        return re
        