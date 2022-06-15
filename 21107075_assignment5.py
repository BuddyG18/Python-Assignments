# 1
string= input('Enter the string to be reversed: ')
i=len(string)-1
rev_string=''
while i>-1:
    rev_string= rev_string+string[i]
    i=i-1
print(f'The reversed string is- {rev_string}')    



# 2
user_range1= int(input('Specify the range for which the divisibles are to be printed- '))
num= int(input('Specify the number for which it\'s divisibles are to be printed- '))
for i in range(user_range1+1):
    if i%num==0:
        print(i)



# 3
import math
a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
if a+b>c and a+c>b and b+c>a:
    print("Area of the triangle is: ",round(area,2))
else:
    print('The sides are invalid.')    




# 4
for i in range(1,5):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(5,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')



# 5
rows= int(input('Number of rows: '))
asciichr = 65

for i in range(0,rows):
    for j in range(0,i+1):
        char = chr(asciichr)
        print(char,end="")
        if asciichr<=89:
            asciichr += 1
        else:
            asciichr -= 26
            asciichr +=1
    print()



# 6
user_range = int(input ("Enter the range: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (user_range + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number) 



# 7 
required_nums=[]
for i in range(1,501):
    if i%7==0 and i%11==0: 
        required_nums.append(i) 
    
print(f'The numbers which are multiples of 7 and divisible by 11 are- {required_nums}')



# 8
user_list1= list(map(int,input('Enter 10 elements of list separated by a single space: ').split()))
positive_nums= []
negative_nums= []
even_nums= []
odd_nums= []
for num in user_list1:
    if num>0:
        positive_nums.append(num)
    elif num<0:
        negative_nums.append(num)
    if num%2==0:
        even_nums.append(num)
    elif num%2!=0:
        odd_nums.append(num)    
# a.
print('The positive numbers in the list are- ', positive_nums)
# b.
print('The negative numbers in the list are- ', negative_nums)
# c.
print('The odd numbers in the list are- ', odd_nums)
# d.
print('The even numbers in the list are- ', even_nums)
# e.
count= {}
for num in user_list1:
    if num not in count:
        count[num]=1
    else:
        count[num] = count[num] + 1   
for key in count:
    print(f'{key} occurs {count[key]} time(s)') 



# 9
count= {}
user_list2= input('Enter the elements of list separated by a single space: ').split()
# print(user_list)
for word in user_list2:
    if word not in count:
        count[word]=1
    else:
        count[word] = count[word] + 1   
for key in count:
    print(f'{key} occurs {count[key]} time(s)')         



