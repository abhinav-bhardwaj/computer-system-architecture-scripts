def calclen(num1,num2):
    a = len(num1)
    b = len(num2)
    if a!=b:
        if a>b:
            for _ in range(a-b):
                num2='0'+num2
        else:
            for _ in range(b-a):
                num1='0'+num1
    
    while len(num1)!=8 and len(num2)!=8:
        num1='0'+num1
        num2='0'+num2

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

def compone(num):
    n = len(num)
    ones=""
    # replacing '1' with '0' and vice-versa for 1's compeslement
    for i in range(n):
        if num[i]=='0':
            ones+='1'
        else:
            ones+='0'
    
    return ones

def comptwo(num):
    n = len(num)
    ones = compone(num)
    # making a list of ones elements because string does not support asssignment
    twos = list(ones.strip("")) 
    # loop running from right of the string to the left
    for i in range(n-1,-1,-1):
        if ones[i] == '1':
            twos[i] = '0'
        else:
            twos[i] = '1'
            break 
        # when '0' is replaced by '1' exits loop
        # because no changes will occur beyond that

    i-=1 # in the case of all 1 e.g 111, 
    # we have to add '1' at the starting position after 2's complement
    if i==-1:
        twos.insert(0,'1')
    twos = "".join(twos)
    return twos

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

    return summ

def bit_sub(num1,num2):
    x,y = num1,num2
    num2 = comptwo(num2)
    sub = bit_add(num1,num2)
    if y>x:
        sub = comptwo(sub)
    else:
        if sub[0]=='1':
            sub = sub[1:]
    return sub

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
bnum1 = fromdectobin(num1,10,2)
bnum2 = fromdectobin(num2,10,2)
bnum1,bnum2 = calclen(bnum1,bnum2)
print("The binary of",num1,"is",bnum1)
print("The binary of",num2,"is",bnum2)
print("Bitwise Subtraction using 2's Complement of numbers",num1,"and",num2,"is",bit_sub(bnum1,bnum2))