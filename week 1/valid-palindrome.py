class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=ord('a')-1
        u=ord('z')   
        left=0
        right=len(s)-1
        while left<right:
            if s[left].isalnum() != True:
                left+=1
            elif s[right].isalnum() !=True:
                right-=1
            else:
                if s[left].lower()!=s[right].lower():
                    return False
                else:
                    right-=1
                    left+=1
        return True

        