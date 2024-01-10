class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        dect=Counter(s2[0:len(s1)])
        dect1=Counter(s1)
        print(dect,dect1)
        left=0
        if dect==dect1:
                return True
        for i in range(len(s1),len(s2)):
            dect[s2[left]]-=1
            dect[s2[i]]+=1
            left+=1
            if dect==dect1:
                return True

        return False
        