class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        ma=0
        dect=defaultdict(int)
        for i in range(len(fruits)):
            dect[fruits[i]]+=1
            while  len(dect)>2:
                dect[fruits[left]]-=1
                if dect[fruits [left]]==0:
                    dect.pop(fruits[left])  
                left+=1
            ma=max(ma,i-left+1)
        return ma
            



        