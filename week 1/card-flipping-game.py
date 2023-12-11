class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
      
        non_flipaable=[]
        for i in range(len(backs)):
            if fronts[i]==backs[i]:
                non_flipaable.append(backs[i])
        min_ba=float("inf")
        min_fr=float("inf")
        print(non_flipaable)
        for i in range(len(fronts)) :
            if fronts[i] not in non_flipaable:
                if min_fr>fronts[i]:
                    min_fr=fronts[i]

        for i in range(len(backs)):
            if backs[i] not in non_flipaable:
               if min_ba>backs[i]:
                   min_ba=backs[i]
        if min(min_fr,min_ba)==float("inf"):
            return 0
        return min(min_fr,min_ba)


                
        

        