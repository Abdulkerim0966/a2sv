class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        su=skill[left]+skill[right]
        ans=0
        while left<right:
            if skill[left]+skill[right]!=su:
                return -1
            else:
                ans+=(skill[left]*skill[right])
                right-=1
                left+=1
        return ans
