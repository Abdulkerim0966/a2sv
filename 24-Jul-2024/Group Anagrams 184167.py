# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def so(s):
            temp = list(s)
            temp.sort()
            temp =''.join(temp)
       
            return temp
        strs.sort(key=lambda x:so(x))

        ans =[[strs[0]]]
        pre =Counter(strs[0])
        for i in range(1,len(strs)):
            now =Counter(strs[i])
            if pre == now:
                ans[-1].append(strs[i])
            else:
                ans.append([strs[i]])
            pre =now
            
        return ans


        