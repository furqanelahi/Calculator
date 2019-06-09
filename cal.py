num_1=int(input("Enter Number one "))
num_2=int(input("Enter Number two "))
opr=input("Enter Operator ")
if opr =='+':
    a=num_1+num_2
    print(a)
elif opr=='-':
    a=num_1-num_2
    print(a)
elif opr =='*':
    a=num_1*num_2
    print(a)
elif opr=='//':
    a=num_1//num_2
    print(a)
else:
    print("Wrong Operator Entered")

print("your calculation is done")