"""
3 mark as input
 tatal
average
result
if pass grade
 90-100 A
 80-89 B
 70-79 C
 else D
 """

m1=int(input("Enter the mark1:"))
m2=int(input("Enter the mark2:"))
m3=int(input("Enter the mark3:"))
total=m1+m2+m3
average=total /3.0
print(total)
print(average)

if m1>=35 and m2>=35 and m3>=35:
    print("Result : Pass")
    if average>=90 and average<=100:
        print("Grade: A")
    if average>=80 and average<=89:
        print("Grade: B")
    if average>=70 and average<=79:
        print("Grade: C")
else:
    print("Result: fail")
    print("Grade: no grade")



