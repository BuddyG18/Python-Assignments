# 1
marks= int(input("Enter your marks: "))
if marks>=80:
    print("Your grade is- A")
elif 60<=marks<80:
    print("Your grade is- B")
elif 50<=marks<60:
    print("Your grade is- C")
elif 45<=marks<50:
    print("Your grade is- D")
elif 25<=marks<45:
    print("Your grade is- E")  
elif marks<25:
    print("Your grade is- F")        



# 2
year= int(input('Enter the year to be checked: '))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print('Leap year')
        else:
            print('Not a leap year')    
    else:
        print('Leap year')  
else:
    print('Not a leap year')                      



# 3
import random
num_1=random.randint(1,10)
num_2=random.randint(1,10)
num_3= (num_1)*(num_2)
print(f'{num_1} x {num_2} = ',end='')
in_num= int(input())
if in_num == num_3:
    print("Right!")
else:
    print(f'Wrong. The answer is {num_3}.')  



# 4
for i in range (200):
    if i%5==2 and i%6==3 and i%7==2:
        print('Candies in bowl:',i)
