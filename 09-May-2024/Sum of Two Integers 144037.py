# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        a = bin(a)
        f1 = True
        if a[0] =='-':
            a= a[3:] 
            f1= False 
        else: a =a[2:]
        b= bin(b)
        f2 = True
        if b[0] =='-':
            b= b[3:] 
            f2 = False 
        else: b = b[2:]
        
        ans =[]
        ca =0
        poi1 =len(a)-1
        poi2 = len(b)-1
        # print((f1^f2))
        if not(f1^f2):
            # print("g")
            while poi1 >-1 or poi2 >-1:
                
                if poi1 >-1 and poi2 >-1:
                 
                    temp = ca + int(a[poi1]) + int(b[poi2])
                    if temp < 2:
                       
                        ans.append(str(temp))
                        ca =0
                        
                    elif temp ==2:
                        ca =1
                        ans.append(str(0))
                    else:
                        ca =1
                        ans.append(str(1))
                    poi1 -= 1
                    poi2 -= 1
              
                elif poi1 >-1:
                    temp = ca + int(a[poi1])
                    if temp < 2:
                        ans.append(str(temp))
                        ca =0
                    elif temp ==2:
                        ca =1
                        ans.append(str(0))
                    poi1 -=1

                else:
                 
                    temp = ca + int(b[poi2])
                    if temp < 2:
               
                        ans.append(str(temp))
        
                        ca =0
                    elif temp == 2:
                        ca =1
                        ans.append(str(0))
                    poi2 -=1
            if ca:
                ans.append('1')
            return int(''.join(reversed(ans)),2) if f1 else -int(''.join(reversed(ans)),2)
        else:
            if f2:
                a,b = b,a
                poi1 ,poi2 =poi2,poi1
            # print (a,b)
            if int (a,2) >int(b,2):
                while poi1 >-1 or poi2 >-1:
                
                    if poi1 >-1 and poi2 >-1:
                    
                        temp = int(a[poi1]) - int(b[poi2]) - ca
                        if temp >-1 :
                            # print("jrn")
                            ans.append(str(temp))
                            ca =0
                            
                        elif temp == -1:
                            # print('hre')
                            ca =1
                            ans.append(str(1))
                        else:
                            # print('hredddd')
                            ca =1
                            ans.append(str(0))
                        poi1 -= 1
                        poi2 -= 1
                        print(ans)
                    elif poi1 >-1:
                        temp =  int(a[poi1]) -ca
                        if temp > -1:
                            ans.append(str(temp))
                            ca =0
                        elif temp == -1:
                            ca =1
                            ans.append(str(1))
                        poi1 -=1

                # print (ans)
                return int(''.join(reversed(ans)),2)

            else:
                a,b = b,a
                poi1 ,poi2 =poi2,poi1
                while poi1 >-1 or poi2 >-1:
                
                    if poi1 >-1 and poi2 >-1:
                    
                        temp = int(a[poi1]) - int(b[poi2]) - ca
                        if temp >-1 :
                            # print("jrn")
                            ans.append(str(temp))
                            ca =0
                            
                        elif temp == -1:
                            ca =1
                            ans.append(str(1))
                        else:
                            ca =1
                            ans.append(str(0))
                        poi1 -= 1
                        poi2 -= 1
                        # print(ans)
                    elif poi1 >-1:
                        temp = int(a[poi1]) - ca
                        if temp > -1:
                            ans.append(str(temp))
                            ca =0
                        elif temp == -1:
                            ca =1
                            ans.append(str(1))
                        poi1 -=1
                return -int(''.join(reversed(ans)),2)
                
            
        

        
        