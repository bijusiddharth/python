"""s="biju siju"
print(s)
print(type(s))
print(s.upper())#all letter change to capitial
print(s.lower())#all letter change to small
print(s.capitalize())#first letter change to capitial
print(s.title())#line first letter change to capitial
print(s.count("i"))#it is counting a particilar letter
print(s.endswith("u"))# this is last letter cheking
print(s.find("s"))#find the letter 
print(s.find("i",5))#this find to above 5th index
print(s.replace("i","0"))#replace letter

a="biju1234"
print("its upper:",a.isupper())#true or flas check
print("its upper:",a.islower())#true or flas check
print("is alpha numeric:", a.isalnum())#mix letter and number
print("is alpha:", a.isalpha())#letter check

b="s.\nbiju"#\t space, \n is next line
print(b)
print(b.splitlines())#\n is save to list in singel name
print(b.splitlines(True))

c="i love to it jobes"
print(c.split(" "))

d="i,love,to,it,jobes"
print(d.split(" , "))"""

e="  sbiju  "
print(len(e))
print(len(e.strip()))#total letter
print(len(e.lstrip()))
print(len(e.rstrip()))

f='12-10-2001'
print(f.partition('-'))



 
