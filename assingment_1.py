# assigment one qution
# quetion - 1
num = int(input('enter our num : '))
if num > 0 :
    print( 'positive')
    if num % 2==0 :
        print('even')
    else:
        print('odd')
elif num == 0:
    print('zero')
else : 
    print('negative')

# quetion - 2 
num_1= int(input('enter our num_1 : '))
num_2= int(input('enter our num_2 : '))
num_3= int(input('enter our num_3 : '))
if num_1 > num_2 and num_2 > num_3 :
    print('num_1 is graeter')
elif num_2 > num_1 and num_1 > num_3 :
    print('num_2 is greater')
else :
    print('num_3 is greater')

# question - 3 
marks= int(input('enter our marks : '))
if marks >= 90 :
    print('Grade A, PASS')
elif marks >= 80 :
    print('Grade B , PASS')
elif marks >= 60:
    print('Grade C,PASS')
elif marks >= 40 :
    print('Grdae D , PASS')
else :
    print('FAIL')

# question 
a = int(input('enetr your number :'))
vote_given = int(input('enetr your number :'))
if a>=18  :
    print('a is elgible for voting ')
    if vote_given == 0 :
        print('first time voter')
    else:
        print('not a first time voter')
    
else :
    print('not elgible')    

#question - 5
num = int(input('enetr your number :'))
if num % 5 == 0 :
    print('num is divisble from 5 ')
    if num % 10 == 0 :
        print('num is also divisble from 10')
else :
    print('not divisble')

#question - 6
word = input('enetr your number :')
vowels ="aeiouAEIOU"
if word in vowels :
    print('word is vowel')
else :
    print('not ')  

#question - 7
age = int(input('enetr your age :'))
qualification = input('enetr your pass or not :')
if age >= 20 :
    print('age is eligible')
    if qualification == 'PASS' :
        print('qualified')
    else :
        print('not qualified')
else:
 print('not eligible for job')

#  question - 8 
a = int(input('enetr your number :'))
if a > 50 :
    print('a is grteater then 50')
    if a > 100 :
        print(' a is also greater then 100')
else :
    print('not greater')        

# question- 9 
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# question- 10
m = int(input("Enter marks: "))

if m >= 90 and m <= 100:
    print("Grade A")
elif m >= 80:
    print("Grade B")
elif m >= 70:
    print("Grade C")
elif m >= 60:
    print("Grade D")
else:
    print("Grade F")

# question - 11
d = int(input("Enter day number (1-7): "))

if d == 1:
    print("Monday")
elif d == 2:
    print("Tuesday")
elif d == 3:
    print("Wednesday")
elif d == 4:
    print("Thursday")
elif d == 5:
    print("Friday")
elif d == 6:
    print("Saturday")
elif d == 7:
    print("Sunday")
else:
    print("Invalid day")

# question - 12
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# question - 13
y = int(input("Enter year: "))

if  (y % 4 == 0 and y % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")

# question-14
age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# question-15
ch = input("Enter a character: ")

if ch.lower() in 'aeiou':
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

# question - 16
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("Invalid operator")

# question-17
n = int(input("Enter number: "))

if n % 2 == 0:
    print("Divisible by 2")
elif n % 3 == 0:
    print("Divisible by 3")
elif n % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 2, 3, or 5")

# question-18
m = int(input("Enter month number: "))

if m == 1:
    print("January")
elif m == 2:
    print("February")
elif m == 3:
    print("March")
elif m == 4:
    print("April")
elif m == 5:
    print("May")
elif m == 6:
    print("June")
elif m == 7:
    print("July")
elif m == 8:
    print("August")
elif m == 9:
    print("September")
elif m == 10:
    print("October")
elif m == 11:
    print("November")
elif m == 12:
    print("December")
else:
    print("Invalid month")

# question-19
a = int(input("Side a: "))
b = int(input("Side b: "))
c = int(input("Side c: "))

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

# question - 20
m = int(input("Enter month: "))

if m in (12, 1, 2):
    print("Winter")
elif m in (3, 4, 5):
    print("Summer")
elif m in (6, 7, 8):
    print("Monsoon")
elif m in (9, 10, 11):
    print("Autumn")
else:
    print("Invalid month")

# question - 21
u = int(input("Enter units: "))

if u <= 100:
    bill = u * 1
elif u <= 200:
    bill = 100*1 + (u-100)*2
else:
    bill = 100*1 + 100*2 + (u-200)*3

print("Bill =", bill)

#question-22
n = abs(int(input("Enter number: ")))

if n < 10:
    print("One digit")
elif n < 100:
    print("Two digit")
elif n < 1000:
    print("Three digit")
else:
    print("More than three digits")

# question-23
m = int(input("Enter marks: "))

if m >= 75:
    print("Distinction")
elif m >= 60:
    print("First Class")
elif m >= 50:
    print("Second Class")
elif m >= 35:
    print("Pass")
else:
    print("Fail")

# question-24
p = int(input("Enter percentage: "))

if p >= 90:
    print("Excellent")
elif p >= 75:
    print("Very Good")
elif p >= 60:
    print("Good")
elif p >= 40:
    print("Average")
else:
    print("Poor")

# question-25
c = input("Enter color: ").lower()

if c == "red":
    print("Stop")
elif c == "yellow":
    print("Wait")
elif c == "green":
    print("Go")
else:
    print("Invalid color")

#question-26
n = int(input("Enter number: "))

if n == 0:
    print("Zero")
elif n > 0 and n % 2 == 0:
    print("Positive Even")
elif n > 0 and n % 2 != 0:
    print("Positive Odd")
else:
    print("Negative")
