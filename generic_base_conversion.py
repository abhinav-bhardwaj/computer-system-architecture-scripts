def alphanum(n):
    if n>= '0' and n<='9':
        return ord(n) - ord('0')
    else:
        return ord(n) - ord('A') + 10

def fromdectoany(num,baseA,baseB):
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

def todecimal(num,baseA,baseB):
    dec = 0
    l = len(str(num))
    num = "".join(reversed(num))
    for i in range(l):
        n = alphanum(num[i])
        if (n >= baseA):
            print("Invalid Number!")
            return -1
        dec = dec + n*pow(baseA,i)
    return dec

def tohexa(num,baseA,baseB):
    num = todecimal(num,baseA,baseB)
    if (num==-1):
        return -1
    if baseB==10:
        return num
    hex = fromdectoany(num,baseA,baseB)
    return hex

def tooctal(num,baseA,baseB):
    num = todecimal(num,baseA,baseB)
    if (num==-1):
        return -1
    if baseB==10:
        return num
    oct = fromdectoany(num,baseA,baseB)
    return oct

def tobin(num,baseA,baseB):
    num = todecimal(num,baseA,baseB)
    if (num==-1):
        return -1
    if baseB==10:
        return num
    bin = fromdectoany(num,baseA,baseB)
    return bin

def main():
    baseA = int(input("Enter from which base you want to convert (in digit) : "))
    print("Enter number of base ",baseA," : ")
    num = input()
    baseB = int(input("Enter to which base you want to convert (in digit) : "))
    if (baseB==10):
        conv = todecimal(num,baseA,baseB)
    elif (baseB==16):
        conv = tohexa(num,baseA,baseB)
    elif (baseB==8):
        conv = tooctal(num,baseA,baseB)
    elif (baseB==2):
        conv = tobin(num,baseA,baseB)
    else:
        print("Invalid Base!")
        return
    
    if(conv==-1):
        return
    print("Given number {} of base {} is converted into base {} and value is {}".format(num,baseA,baseB,conv))
    return

main()