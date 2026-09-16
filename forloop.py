# #for loop
# str="Python"
# for s in str:
#     print(s)

# #in for loop print single character with positive index or negative index in same line 

# s="python"
# i=0
# for i in str:
#     print(s,"+ve",i,"-ve",i-len(str))
#     i+=1

#print 0 to 10 in for loop
#print odd number from 1 to 20
#print 10 to 1
#Accept list from user and print sum of list

# for i in (0,1,2,3,4,5,6,7,8,9,10):
#     print(i)

# print("**************************************")

# for i in (1,2,3,4,5,6,7,8,9,10):
#     print(i)

# print("**************************************")

# for i in (10,9,8,7,6,5,4,3,2,1):
#     print(i)

# print("**************************************")


# lst = eval(input("Enter list: "))

# total = 0

# for i in lst:
#     total += i

# print("Sum =", total)

# print("**************************************")

# i=0
# while i<5:
#     print("Hello")
#     i+=1

# print("**************************************")

#Accept a number from user and print its table 
#Accept a number and print its factorial
#Accept a number and print its reverse
# n=234 432
#Accept name from user until its your name

n = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

# # print("**************************************")

n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i += 1

print("Factorial =", fact)

# print("**************************************")

n = int(input("Enter a number: "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse =", rev)








