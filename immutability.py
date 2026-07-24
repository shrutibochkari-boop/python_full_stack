a=10
b=10
c=55
print("a=",a)
print("b=",b)
print("Address of a",id(a))
print("Address of b",id(b))
print("Address of c",id(c))
b=32
print("Address of a",id(a))
print("Address of b",id(b))
print("Address of c",id(c))

print("***********************************************")

#String
a="shruti"
b="shruti"
c="nishu"
print("a=",a)
print("b=",b)
print("Address of a",id(a))
print("Address of b",id(b))
print("Address of c",id(c))
b="java"
print("Address of a",id(a))
print("Address of b",id(b))
print("Address of c",id(c))

print("***********************************************")


#List 
#Mutable

l1=[10,20,30]
l2=[10,20,30]
print("l1=",l1)
print("l2=",l2)
print("Address of l1",id(l1))
print("Address of l2",id(l2))

l1[2]=66
print("l1=",l1)
print("l2=",l2)
print("Address of l1",id(l1))
print("Address of l2",id(l2))

print("***********************************************")

#datatype
#byte immutable
#bytearray mutable


#byte
x=[10,20,30,40]
print("type of x:",type(x))
b=bytes(x)
print("type of b:",type(b))
x[0]=78
print("b=",b)
print(b[2])

print("**********************************************")

#bytearray
x=[10,20,30,40]
print("type of x:",type(x))
b=bytearray(x)
print("b=",b)
print("type of b:",type(b))
b[0]=100
print("b=",b)
for i in b:
    print("i=",i)

print("**********************************************")

#list---mutable

l1=[10,20,"Python",30,10]
print(l1)
print(type(l1))
print(l1[3])
print(l1[2:])
l1.append(100)
print(l1)
l1.remove(30)
print(l1)

print("**********************************************")

#tuple---immutable

t=(10,20,30,"python",2.32,60)
print(t)
print(type(t))
print(t[3])
print(t[-1:-4:-1])

t=() #empty tuple
print(t)
print(type(t))

t=(10,) #single value tuple
print(t)
print(type(t))
print("**********************************************")


#range---immutable

r=range(0,20,2)
print(r)
for i in r:
  print(r)

for i in range(1,11,2):
 print (i)


for i in range(10,0,-1):
 print(i)



print("**********************************************")

#set ---mutable

s={10,20,30,"python",44,44.5}
print(s)
print(type(s))
s.add("java")
print(s)
print(type(s))

s={} #dictionary
print(s)
print(type(s))

s=set()
print(s)
print(type(s))
