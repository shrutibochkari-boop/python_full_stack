#ladder if else

n1=int(input("Enter 1st number"))
n2=int(input("Enter 2nd number"))
n3=int(input("Enter 3rd number"))
if n1>n2 and n1>n3:
    print("n1 is max")
elif n2>n3:
    print("n2 is max")
else:
    print("n3 is max")
