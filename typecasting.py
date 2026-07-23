#typecasting

#int

a=112.45 #float
a=False #boolean
a="21" #string
x=int(a)
print("a=",a)
print("x=",x)
print("datatype",type(a))
print("datatype",type(x))
print(a+a) #concantention since it is a string
print(x+x) #addition since it is int

print("***********************************************")
#float
a=23 #int

x=float(a)
print("a=",a)
print("x=",x)
print("datatype",type(a))
print("datatype",type(x))

print("*************************************")

#complex(n,m)

a=2
b=2.4
print(complex(a,b))

#complex(n)

a=2
a=2.5
#a=True
#a="5"
print(complex(a))

print("********************************************")

#boolean

#a=2
#a=0.00
#a="23"
a=2+3j
print(bool(a))
print("datatype",type(a))

print("**********************************************")

#string

#a=2.2
a=True
x=str(a)
print("a=",a)
print("x=",x)
print("datatype",type(a))
print("datatype",type(x))

n=14.55
i=(int(n))
d= n-i
print("i=",i)
print("d=",d)



