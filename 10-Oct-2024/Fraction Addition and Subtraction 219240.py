# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, expression: str) -> str:
        stacks =[]
        stack1 =[]
        stack2 =[]

        l =len(expression)
        i =0
        if expression[0] == "-":
            stacks.append(expression[i])
            i+=1
        else:
            stacks.append("+")

        while i < l:
            if expression[i] == "+" or expression[i] =="-":
                stacks.append(expression[i])
                i+=1
            temp=''
            while expression[i] != "/" and i< l:
                temp+=expression[i]
                i+=1
            stack1.append(int(temp))
            i+=1
            temp =""
            while i< l and (expression[i] != "+" and expression[i] != "-")  :
                temp+=expression[i]
                i+=1
            stack2 .append(int(temp))
        total =1
        for i in range(len(stack2)):
            total *=(stack2[i])

        ans =0
        for i in range(len(stack1)):
            temp = stack1[i]*(total//stack2[i])
            if stacks[i] =="-":
                ans -=temp
            else:
                ans+= temp
        temp = gcd(ans,total)
        ans/=temp
        total /=temp

        return (str(int(ans))+"/"+str(int(total)))






        