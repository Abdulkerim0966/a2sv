# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        dect= defaultdict(list)
        requir = defaultdict(int)
        supply = set(supplies)

        for i in range (len(recipes)):
            for j in range(len(ingredients[i])):
                dect[ingredients[i][j]].append(recipes[i])
                requir[recipes[i]] +=1
        
        que = deque()
        for item in supplies:
            if requir[item] ==0:
                que.append(item)
            
        ans=[]
        while que:
            temp = que.popleft()
            for nigh in dect[temp]:
                requir[nigh] -=1

                if requir[nigh] ==0:
                    ans.append(nigh)
                    que.append(nigh)

        return ans

















            