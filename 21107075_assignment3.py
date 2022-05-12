# 1
num= int(input("Type any number: "))
print(bin(num))



# 2
a = input('Enter a mathematical expression: ')
print(a,'=',eval(a))



# 3
import math
# a)
print('a)')
exp= (3+4)*5
print(exp)
# b)
print('b)')
n= float(input("Specify the value of n to be used in expression n(n-1)/2 : "))
exp_2= (n*(n-1))/2
print("Resultant value:",exp_2)
# c)
print('c)')
r= float(input("Specify the value of r to be used in expression 4πr^2 : "))
exp_3= 4*math.pi*r*r 
print(exp_3)
# d)
print('d)')
r= float(input("Specify the value of r: "))
a= float(input("Enter first angle: "))
b= float(input("Enter second angle: "))
print(math.sqrt((r*math.cos(a)**2) + (r*math.sin(b)**2)))
# e)
print('e)')
x1 = float(input('Enter x coordinate of first point: '))
y1 = float(input('Enter y coordinate of first point: '))
x2 = float(input('Enter x coordinate of second point: '))
y2 = float(input('Enter y coordinate of second point: '))
print((y2-y1)/(x2-x1))



# 4
# a)
print('a)')
for i in range(5):
    print(i)
# b)
print('b)')
for i in range(3,10):
    print(i)
# c)
print('c)')
for i in range(4,13,3):
    print(i)
# d)
print('d)')
for i in range(15,5,-2):
    print(i)
# e)
print('e)')
for i in range(5,3): # If a user wants to decrement, then the user needs steps to be a negative number
    print(i)



# 5 
h_atoms= int(input("Number of Hydrogen atoms in the molecule: "))
o_atoms= int(input("Number of Oxygen atoms in the molecule: "))
c_atoms= int(input("Number of Carbon atoms in the molecule: "))
mol_wt= (h_atoms*1.00794) + (o_atoms*15.9994) + (c_atoms*12.0107)
print(mol_wt)