# #accept two numbers from user and print max of those 2 number in ternery operator

a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))


print("Maximum number is:", a if a > b else b)

# #accept age from user the print whether eligible for voting or not

age=int(input("Enter a age:"))
print("Eligible for voting" if age >= 18 else "Not eligible for voting")

# #Accept a number from user and prinrt wheather it is even or odd

num=int(input("Enter a number:"))
print("The number is even" if num %2==0 else "The number is odd")


a=int(input("Enter Employee no:"))
b=(input("Enter Employee name:"))
c=float(input("Enter Employee salary:"))
d=bool(input("Married?[True|False]"))

print("Please confirm Information")
print("Enter employee no:",a)
print("Enter employee name:",b)
print("Enter employee salary:",c)
print("Employee Married?")

# Accept two numbers and print max of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

max_num = b
if a > b:
    max_num = a

print("Maximum number is:", max_num)

#Accept a number and print absolute of that number

num = int(input("Enter a number: "))

if num < 0:
    num = -num

print("Absolute value is:", num)

#accept a number and print wheather itb is neagative or positive

num = int(input("Enter a number: "))

if num >= 0:
    print("Positive Number")
else:
    print("Negative Number")

#Accept 2 numbers from command prompt and print max of those 2 numbers

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

if a > b:
    print("Maximum number is:", a)
else:
    print("Maximum number is:", b)


