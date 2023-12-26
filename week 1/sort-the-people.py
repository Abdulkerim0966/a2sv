class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(names)-1
        while n>0:
            for i in range(n):
                if heights[i]>heights[i+1]:
                    heights[i],heights[i+1]=heights[i+1],heights[i]

                    names[i],names[i+1]=names[i+1],names[i]
            n-=1
        names.reverse()
        return names


        