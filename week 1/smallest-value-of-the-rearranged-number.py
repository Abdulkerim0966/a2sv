class Solution:
    def smallestNumber(self, num: int) -> int:   

        if num>=0:
            st=list(str(num))
            for i in range(len(st)):
                for j in range(len(st)-i-1):
                    if int(st[j])>int(st[j+1]):
                        st[j],st[j+1]=st[j+1],st[j]
            for i in range(len(st)):
                if st[i]!='0':
                    break
                else:
                    for j in range(1,len(st)):
                        if st[j]!='0':
                            st[0],st[j]=st[j],st[0]
                            break
                    break
            print (int(''.join(st)))
            return (int(''.join(st)))
        else:
            st=list(str(abs(num)))
            for i in range(len(st)):
                for j in range(len(st)-i-1):
                    if int(st[j])<int(st[j+1]):
                        st[j],st[j+1]=st[j+1],st[j]
            
            
            return (0-(int(''.join(st))))
            

    
        