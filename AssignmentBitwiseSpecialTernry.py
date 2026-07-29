#Assignment opetaor 
#short and compound operator
a=10
b=5
a+=b
a-=b
a*=b
a/=b
a**=b
a%=b
print(a)

print("***********************************")

#Bitwise operator & | ^
a=4
b=6
print(a&b)
print(a|b)
print(a^b)

#right shift left shift << >>

print(10<<2)
print(10>>2)

#identity operator----use for address comaprasion (is is not)

n1=10
n2=10
print("address n1:",id(n1))
print("address n2",id(n2))
print(n1 is n2)
print(n1 is not n2)

l1=[10,20,"python"]
l2=[10,20,"python"]
print("address n1:",id(l1))
print("address n2",id(l2))
print(l1 is l2)
print(l1 is not l2)
print(l1==l2)

#memebership operator--in not in
l1=[10,20,"python"]
x=20
print(x in l1)
print(x not in l2)

#Ternary operator

a=int(input("Emter a number:"))
res= "yes" if a<40 else "no"
print(res)

#accept two numbers from user and print max of those 2 number in ternery operator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

maximum = num1 if num1 > num2 else num2

print("Maximum number is:", maximum)

#accept age from user the print whether eligible for voting or not

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")



