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

def bit_add(num1,num2):
    carry="0"
    summ=""
    for i in range(len(num1)-1,-1,-1):
        if num1[i]=='0' and num2[i]=='0':
            if carry=='1':
                summ='1'+summ
                carry='0'
            else:
                summ='0'+summ
        elif num1[i]=='1' and num2[i]=='1':
            if carry=='1':
                summ='1'+summ
            else:
                summ='0'+summ
                carry='1'
        elif ((num1[i]=='1' and num2[i]=='0') or (num1[i]=='0' and num2[i]=='1')):
            if carry=='1':
                summ='0'+summ
            else:
                summ='1'+summ

    if carry=='1':
        summ='1'+summ
    print("Bitwise Addition of",num1,"and",num2,"is",summ)
    return

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
bnum1 = fromdectobin(num1,10,2)
bnum2 = fromdectobin(num2,10,2)
bnum1,bnum2 = calclen(bnum1,bnum2)
print("The binary of",num1,"is",bnum1)
print("The binary of",num2,"is",bnum2)
bit_add(bnum1,bnum2)