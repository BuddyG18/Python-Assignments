# 1
number_1= float(input('Enter First Number: '))
number_2= float(input('Enter Second Number: '))
number_3= float(input('Enter Third Number: '))
average= (number_1 + number_2 + number_3)/3
print(average)

# 2
gross_income= float(input("Your Gross income- "))
no_of_dependents= float(input("Number of dependents- "))
dependent_deduction= 3000
standard_deduction= 10000
taxable_income = gross_income - standard_deduction - (dependent_deduction * no_of_dependents)
tax_rate= 0.2
tax = taxable_income * tax_rate
print(f'Tax- ${tax}')

# 3
seconds= int(float(input("number of seconds: ")))
minutes= seconds//60 
remaining_seconds= seconds%60
print(minutes,"minutes and",remaining_seconds,"seconds")

# 4
result= str(25+int(float('25')+int(25.0)))
print(result)

#5
import math
for i in range(0,346,15):
    angle = i*(math.pi)/180
    print(f'{i} --- {round((math.sin(angle)),4)} {round((math.cos(angle)),4)}')
    







