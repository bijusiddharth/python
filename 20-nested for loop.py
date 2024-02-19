"""
A-Z =>65-95
a-z=>97-122
"""

for i in range(6):
    for j in range(i):
        print("*",end="")
    print("")

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")

for i in range(65,72,1):
    for j in range(65,72,1):
        print(chr(j),end="")
    print("")

