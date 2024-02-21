class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dect=Counter()
        for i in range(len(bills)):
            if bills[i]==5:
                dect[5]+=1
            elif bills[i]==10:
                if dect[5]==0:
                    return False
                else:
                    dect[5]-=1
                    dect[10]+=1
            else:
                if dect[5]==0 or (dect[10]==0 and dect[5]<3):
                    return False
                else:
                    if dect[10]==0:
                        dect[5]-=3
                    else:
                        dect[10]-=1
                        dect[5]-=1
        return True


        