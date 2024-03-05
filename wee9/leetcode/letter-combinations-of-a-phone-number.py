class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        bucket=[]
        ans=[]
        dect={}
        dect['2']='abc'
        dect['3']='def'
        dect['4']='ghi'
        dect['5']='jkl'
        dect['6']='mno'
        dect['7']='pqrs'
        dect['8']='tuv'
        dect['9']='wxyz'
        print(dect)
        n=len(digits)
        def backtrack(idx):
            
            if len(bucket)==n:
                if bucket:
                    ans.append(''.join(bucket.copy()))
                return 
        


            for i in range(len(dect[digits[idx]])):

                bucket.append(dect[digits[idx]][i])
                backtrack(idx+1)
                bucket.pop()
               
        backtrack(0)


        return ans
        