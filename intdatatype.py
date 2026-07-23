#int
#binary from---prefix 0b or 0B allowed digit 0 or 1

a=0B101
print("a=",a)
print(type(a))

#octal form --prefix 0o or 0O allowed digit 0 or 7

a=0o145
print("a=",a)
print(type(a))

#Hexa decimal -- prefix 0x or oX allowed digit 0 to 9, a-f

a=0Xab24
print("a=",a)
print(type(a))

#int 
#base conversion
#a)bin()

a=10
print(bin(a))
# b=bin(a)
# print(a)
# print(b)

#octal to binary
a=0o145
print(bin(a))

#hexadecimal to binary
a=0xab34
print(bin(a))

#b oct()
a=10
print(oct(a))

#binary to octal
a=0b101
print(oct(a))

#Hexa to octal
a=0Xab13
print(oct(a))

#hexa hex()

#decimal to hexa
a=10
print(hex(a))

#binary to hexa
a=0b101
print(hex(a))

#octal to hexa
a=0o111
print(hex(a))

#float data type 

f=134.3e0
print("f=",f)
print("Data type of f:",type(f))
print("Address of f:",id(f))

