# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dect= defaultdict(list)

        for i in range(len(accounts)):
            dect[i].extend(accounts[i])
            
        root = [i for i in range(len(accounts))]
        print(root)
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
                # print('here')
                if root[rootX] < root[rootY]:
            
                    root[rootY] = root[rootX]
                else:
                    root[rootX] = root[rootY]
               
               
        dect = defaultdict(int)            
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] in dect:
                    union(dect[accounts[i][j]],i)
                else:
                    dect[accounts[i][j]] = i
        # print(root)
        ans = []
      
        for i in range(len(accounts)):
            if root[i] == i:
                ans.append(accounts[i])
            else:
                rootx = find(i)
                ans[rootx].extend(accounts[i])
                ans.append([])
        temp = []
        for i in range(len(ans)):
            temp1=[]
            if ans[i]:
                temp1.append(ans[i][0])
                temp3 = set(ans[i])
                temp3.remove(temp1[0])
                temp3 = list(temp3)
                temp3.sort()
                temp1.extend(temp3)
                temp.append(temp1)

        return temp


            
            
      













                
        
        
        