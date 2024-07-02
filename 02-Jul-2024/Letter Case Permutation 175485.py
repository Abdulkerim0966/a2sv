# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
     
        def backtrack(idx,temp):
           
            if idx == len(s):
          
                ans.append(''.join(temp))
                return
            if not s[idx].isdigit():
                temp.append(s[idx].lower())
                backtrack(idx+1,temp)
                temp.pop()

                temp.append(s[idx].upper())
                backtrack(idx+1,temp)
                temp.pop()
            else:
                temp.append(s[idx])
                backtrack(idx+1,temp)
                temp.pop()


        backtrack(0,[])
        return ans




        