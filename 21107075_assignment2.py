# 1
# a.
given_string= "Python is a case sensitive language"
length= len(given_string)
print(length)

# b. 
print(given_string[::-1])

# c. 
substring= given_string[10:26]
print(substring)

# d.
print(given_string[:10]+"object oriented"+given_string[26:])

# e.
print(given_string.find('a'))

# f. 
list1= list(given_string.split())
str1= ""
for ele in list1: 
    str1 += ele 
print(str1)




# 2
sid= 21107075
name= 'Dhruv Goyal'
department= 'Mechanical'
cgpa= 9.9 
print('Hey,', name,  'Here!')
print('My SID is', sid)
print('I am from', department, 'department and my CGPA is', cgpa)




# 3
a=56
b=10
# a.
print(a&b)
# b.
print(a|b)
# c.
print(a^b)
# d.
print(a<<2)
print(b<<2)
# e.
print(a>>2)
print(b>>4)




# 4
string= input('Enter something ')
if ('name' in string):
    print("Yes")
else:
    print("No")    




# 5
s1= int(input('Enter first side: '))
s2= int(input('Enter second side: '))
s3= int(input('Enter third side: '))
statement= ((s1+s2)>s3 and (s1+s3)>s2 and (s2+s3)>s1) and (s1>0 and s2>0 and s3>0)
match statement:
    case True:
        print('Yes')
    case False:
        print('No')




# 6
num_1= int(input("Enter first number: "))
num_2= int(input("Enter second number: "))
num_3= bin(num_1^num_2)
num_4= num_3.count('1')
print(num_4)