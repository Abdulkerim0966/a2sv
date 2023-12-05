class Solution:
    def numberOfMatches(self, n: int) -> int:
        wi=n
        count=0
        while wi!=1:
            if wi%2==1:
                count+=int(wi//2)
                wi=(wi//2)+1
            else :
                count+=int(wi/2)
                wi=(wi/2)
        return count
        