# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        root =[i for i in range(len(s))]
        ans = [[s[i]] for i in range(len(s))]
        def find(x):
            while x != root[x]:
                root[x] =root[root[x]]
                x=root[x]
            return x

        def union(x,y):
            parentx = find(x)
            parenty = find(y)

            if parentx != parenty:
                if len(ans[parentx])>len(ans[parenty]):
                    ans[parentx].extend(ans[parenty])
                    root[parenty] = parentx
                else:
                    ans[parenty].extend(ans[parentx])
                    root[parentx] = parenty
        for x,y in pairs:
            union(x,y)
        
        for item in ans:
            heapify(item)
        
        temp = list(s)
        for i in range(len(temp)):
            parent =find(i)
            temp[i] = heappop(ans[parent])
            
        return ''.join(temp)
                    

        