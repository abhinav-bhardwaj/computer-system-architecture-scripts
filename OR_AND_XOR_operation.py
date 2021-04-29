def calclen(num1,num2):
    a = len(num1)
    b = len(num2)
    if a!=b :
        if a>b:
            for _ in range(a-b):
                num2='0'+num2
        else:
            for _ in range(b-a):
                num1='0'+num1
    return num1,num2

def calcor(num1,num2):
    numor=""
    for i in range(len(num1)):
        if num1[i]=='1' or num2[i]=='1':
            numor+='1'
        else:
            numor+='0'
    return numor

def calcand(num1,num2):
    numand=""
    for i in range(len(num1)):
        if num1[i]=='1' and num2[i]=='1':
            numand+='1'
        else:
            numand+='0'
    return numand

def calcxor(num1,num2):
    numxor=""
    for i in range(len(num1)):
        if ((num1[i]=='0' and num2[i]=='0') or (num1[i]=='1'and num2[i]=='1')):
            numxor+='0'
        elif ((num1[i]=='0' and num2[i]=='1') or (num1[i]=='1' and num2[i]=='0')):
            numxor+='1'
    return numxor

def fromdectobin(num,baseA,baseB):
    strr=""
    while num>=1:
        n = num%baseB
        if n>= 0 and n<=9:
            n = chr(n + ord('0')) 
        else:
            n = chr(n - 10 + ord('A')) 
        strr = strr + str(n)
        num = num//baseB
    strr = ''.join(reversed(strr))    
    return strr

num1 = int(input("Enter first integer : "))
num2 = int(input("Enter second integer : "))
bnum1 = fromdectobin(num1,10,2)
bnum2 = fromdectobin(num2,10,2)
bnum1,bnum2 = calclen(bnum1,bnum2)
print("The binary of",num1,"is",bnum1)
print("The binary of",num2,"is",bnum2)
print("OR operation on",num1,"and",num2,"gives",calcor(bnum1,bnum2))
print("AND operation on",num1,"and",num2,"gives",calcand(bnum1,bnum2))
print("XOR operation on",num1,"and",num2,"gives",calcxor(bnum1,bnum2)) 

#SAME RESULT WITH LOGICAL OPERATORS 
#print("OR of 1st Integer by 2nd Integer : ",num1|num2)
#print("AND of 1st integer by 2nd Integer : ",num1&num2)
#rint("XOR of 1st integer by 2nd Integer : ",num1^num2)