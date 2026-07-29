#Input statement

#Evaluate----eval is the convert data into given
#  data 

data=eval(input("Enter a data:"))
print(type(data))
print(data)

#output statement--print() 
#we want and empty line we use print() function only /n=print()
#we want word in next we use (end)

print("Good Morning")
print()
print("How are you")

print("Good",end=" ")
print("Evening")

#Replacement 

name="Tom"
age=30
sal=250000
print(name,"is earning",sal,"and his age",age)
print("{} is earning {} and his age {}".fromat(name,sal,age))
print("{} is earning {} and his age {}".fromat(sal,age,name))
print("{x} is earning {y} and his age {z}".fromat(y=sal,z=age,x=name))
print(f"{name} is earning {sal} and his age {age}")



