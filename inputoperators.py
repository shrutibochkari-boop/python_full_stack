# #operators
# #arithematic operators

# n1=int(input("Enter a number1:"))
# n2=int(input("Enter a number2:"))
# print("Addition:",n1+n2)
# print("Substraction",n1-n2)
# print("Multiplication:",n1*n2)
# print("Division:",n1/n2)
# print("Floor Division:",n1//n2)
# print("Remainder:",n1%n2)
# print("Exponentation:",n1**n2)

# print("*********************************************************")

# #realational operators---> <,>,<=,>=,==,!=

# #A to Z-----65 to 90  askey code
# #a to z ---97 to 122

# a=10
# b=20
# c=a<b
# c=a>b
# c=a<=b
# c=a>=b
# c=a!=b
# c=a==b
# print(c)


# #string use askey code for compare

# s1="Python is easy"
# s2="python"
# print(s1>s2)

#Logical operator

a=10
b=20
c=a>5 and b #c= True and 20
c=a>5 and b-50
c=a>b and b<50
print(c)

#or operator

a=10
b=20
c=a>5 or b #False or 20
c=a>5 or b-50
c=a>b or b<50
print(c)

#not operator
a=""
b="da"
c=not(a>b) #empty string is always False
print(c)

a="python"
b=""
c=not(a)#a(10) not(True) Revers the value true=false false=true
print(c)

#Accept item cost from user . 
# Add sale tax 12%, 
# Octroi 4% and and 
# excise duty 2%
#print the total cost of item


#Accept item cost from user . 
cost=float(input("Enter the cost value:"))

sales_tax=cost*0.12
octroi=cost*0.4
excise_duty=cost*0.2

total_cost=cost+sales_tax+octroi+excise_duty








