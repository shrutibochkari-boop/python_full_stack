#infinite loop

# while True:
#     print("Hello")

#nested loop

# for i in range(3):
#     for j in range(2):
#         print("Hello", end=" ")
#     print()

rows=3
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print()

for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

rows = 3

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end="")
    print()
