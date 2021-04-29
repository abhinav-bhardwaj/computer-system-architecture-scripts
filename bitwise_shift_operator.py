num1 = int(input("Enter first integer : "))
num2 = int(input("Enter second integer : "))

print("Left Shifted 1st integer by 2nd integer : ",num1<<num2)
# Code in the comments gives the correct output as well
#print("Left Shifted 1st integer by 2nd integer : ",num1*(2**num2))
print("Right Shifted 1st integer by 2nd integer : ",num1>>num2)
#print("Right Shifted 1st integer by 2nd integer : ",num1//(2**num2))