print('Enter Your Marks')
number = int(input())
print(number)

if (number>=90 and number<100):
    grade = 'A+'
elif (number>=80 and number<100):
    grade = 'A'
else:
    grade = 'Don\'t know'
print(grade)