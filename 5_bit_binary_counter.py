def bit_inc(num1):
    num1=list(num1)
    if num1[-1] == '0':
        num1[-1]='1'
    else:
        carry='0'
        i = len(num1)-1
        while i>-1:
            if carry=='1' and num1[i]=='1':
                num1[i]='0'
            elif carry=='1' and num1[i]=='0':
                num1[i]='1'
                carry='0'
                break
            elif num1[i]=='1':
                num1[i]='0'
                carry='1'
            elif num1[i]=='0':
                num1[i]='1'
                break
            i-=1
    
    num1 = "".join(num1)
    return num1

nat = input("Choose UP or DOWN nature of 5 bit binary counter : ")

num = "00000"

nums=[num]
i=1
while i<32:
    num = bit_inc(num)
    i+=1
    nums.append(num)

nat = nat.lower()
if nat=='up':
    print(nums)
elif nat=='down':
    nums.reverse()
    print(nums)
else:
    print("Wrong Choice!")
