class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ma=abs(target[0])+abs(target[1])
        an=True
        for i in range(len(ghosts)):
            if ma>=(abs(target[1]-ghosts[i][1])+abs(target[0]-ghosts[i][0])):
                an=False
                break
        return an
        