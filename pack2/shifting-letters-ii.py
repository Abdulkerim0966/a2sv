class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift=[0]*len(s)
        ans=[]
        for sh in shifts:
            start = sh[0]
            end = sh[1]
            if sh[2] == 0:
                shift[start] -= 1
                if end + 1 < len(s):
                    shift[end + 1] += 1
            else:
                shift[start] += 1
                if end + 1 < len(s):
                    shift[end + 1] -= 1
        
        for i in range(1,len(s)):
            shift[i] += shift[i-1]
        for i in range(len(s)):
            ans.append(chr(97+((ord(s[i])-97)+(shift[i])%26)%26))
        return "".join(ans)
        
        

        