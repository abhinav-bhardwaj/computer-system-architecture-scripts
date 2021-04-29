def complement(num):
    n = len(num)
    ones=""
    # replacing '1' with '0' and vice-versa for 1's comeplement
    for i in range(n):
        if num[i]=='0':
            ones+='1'
        else:
            ones+='0'
    
    print("1s complement of",num,":",ones)

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

num = input("Enter a binary value : ")
print("2s complement of",num,":",complement(num))
