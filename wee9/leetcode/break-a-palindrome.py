class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        mid=-1
        flag=False
        ind=0
        if len(palindrome)%2==1:
            mid=(len(palindrome)//2)
        for i in range(len(palindrome)):
            if i!=mid :
                if palindrome[i]!='a':
                    return (palindrome[0:i]+'a'+ palindrome[i+1:])
                else:
                    flag=True
                    ind=i
        if flag==True:
            return (palindrome[0:i]+'b'+ palindrome[i+1:])
        return ''
                
        