# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        root = {s1[i]: s1[i] for i in range(len(s1))}
        root.update({s2[i]: s2[i] for i in range(len(s2))})
        # print(root)
        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x
    
        def union(x, y):
            nonlocal root
            # print(x,y)
            rootX = find(x)
            rootY = find(y)
            # print(rootX,rootY)
            if root[rootX] != root[rootY]:
                print('here')
                if root[rootX] < root[rootY]:
                    root[rootY] = root[rootX]
                else:
                    root[rootX] = root[rootY]
                    
        for i in range(len(s1)):
            union(s1[i],s2[i])
        ans=[]
        # print(root)   
        for i in range(len(baseStr)):
            if baseStr[i] in root:
                ans.append(find(baseStr[i]))
            else:
                ans.append(baseStr[i])
        return ''.join(ans)
                
        