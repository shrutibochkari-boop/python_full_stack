#Accept state from user (Maharashtra,Goa,Karnataka) and print its capital

state = input("Enter state (Maharashtra, Goa, Karnataka): ")

if state == "Maharashtra":
    print("Capital: Mumbai")
elif state == "Goa":
    print("Capital: Panaji")
elif state == "Karnataka":
    print("Capital: Bengaluru")
else:
    print("Invalid state")

#accept marks of 5 subjects calculate percentage and display the class as below
#percentage is above 75----Distinction
#percentage between 60 and 75---first class
#percentage between 50 and 60---second class
#percentage between 40 and 50--pass class
#less than 40     ---fail

s1=float(input("Enter marks of subject 1:"))
s2=float(input("Enter marks of subject 2:"))
s3=float(input("Enter marks of subject 3:"))
s4=float(input("Enter marks of subject 4:"))
s5=float(input("Enter marks of subject 5:"))

total=s1+s2+s3+s4+s5
percentage=total/5

print("Total marks:",total)
print("percentage:",percentage)

if percentage == 75:
    print("Class: Distinction")
elif percentage >= 60:
    print("Class: First Class")
elif percentage >= 50:
    print("Class: Second Class")
elif percentage >= 40:
    print("Class: Pass Class")
else:
    print("Class: Fail")


