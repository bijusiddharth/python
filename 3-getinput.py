name=input("Enter the name: ")
print(name)
print(type(name))

a= int(input("Enter the value A:"))
b=int(input("Enter the value B:"))
c=a+b
print(type(c))

name1,name2,name3=input("Enter the 3names:").split(',')
print("Name1:",name1)
print("Name2:",name2)
print("Name3:",name3)

x=int(input("Enter the number :"))
lista=[10,20,30,40,50]
if x in lista:
    print("yes")
else:
    print("no")

a=input("Enter the name:")
name=["biju","karthi","ram"]
if a not in name:
    print("yes")
else:
    print("no")

a=int(input("Enter the number:"))
if a!="10":
    print("yes")
else:
    print("no")
