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

def selective_clear(A,B):
    n=len(A)
    A = list(A)
    for i in range(n):
        if B[i]=='1':
            if A[i]=='1':
                A[i] = '0'

    A="".join(A)
    return A

A = input("Enter bits of Register A : ")
B = input("Enter bits of Register B : ")
bin_A,bin_B = calclen(A,B)
print("Selective Clear Operation on A =",bin_A,"gives",selective_clear(bin_A,bin_B))
