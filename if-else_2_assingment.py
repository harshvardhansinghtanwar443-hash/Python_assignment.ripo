# 1. 
n = int(input())

if n > 0 and n % 2 == 0 and n % 3 == 0:
    print("Number satisfies all conditions")
else:
    print("Conditions not satisfied")

# 2. 
n = int(input())

if n < 10 or n > 50:
    print("Outside the range")
else:
    print("Inside the range")

# 3. 
age = int(input())

if age >= 18 and age < 60:
    print("Eligible to vote")
else:
    print("Not eligible")

# 4. 
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# 5. 
ch = input()

if ch.isalpha() and ch.lower() in "aeiou":
    print("Alphabet and vowel")
else:
    print("Not an alphabet vowel")

# 6. 
n = int(input())

if (n % 4 == 0 or n % 6 == 0) and not (n % 4 == 0 and n % 6 == 0):
    print("Condition satisfied")
else:
    print("Condition not satisfied")

# 7. 
a = int(input())
b = int(input())
c = int(input())

if a >= 40 and b >= 40 and c >= 40:
    print("Passed all subjects")
else:
    print("Failed")

# 8. 
pwd = input()

if len(pwd) >= 8:
    print("Valid password")
else:
    print("Invalid password")

# 9. 
n = int(input())

if n >= 100 and n <= 999 and n % 2 == 0:
    print("Valid number")
else:
    print("Invalid number")

# 10. 
ch = input()

if ch.isalpha():
    print("Alphabet")
else:
    print("Not an alphabet")

# 11. 
t = int(input())

if t >= 20 and t <= 30:
    print("Comfortable")
else:
    print("Not comfortable")

# 12. 
n = int(input())

if n % 2 == 0:
    print("Divisible by 2")
if n % 3 == 0:
    print("Divisible by 3")
if n % 5 == 0:
    print("Divisible by 5")

# 13. 
age = int(input())
income = int(input())

if age >= 21 and income >= 20000:
    print("Eligible for loan")
else:
    print("Not eligible")

# 14. 
s = input()

if s != "" and len(s) > 8:
    print("Valid string")
else:
    print("Invalid string")

# 15. 
a = int(input())
b = int(input())
c = int(input())

if a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b:
    print("Right angled triangle")
else:
    print("Not right angled")

# 16. 
p = int(input())

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

# 17. 
n = int(input())

if n == 0:
    print("Zero")
elif n > 0 and n % 2 == 0:
    print("Positive Even")
elif n > 0:
    print("Positive Odd")
elif n < 0 and n % 2 == 0:
    print("Negative Even")
else:
    print("Negative Odd")

# 18. 
u = int(input())

if u <= 100:
    bill = u * 1
elif u <= 200:
    bill = u * 2
else:
    bill = u * 3

print(bill)

# 19. 
income = int(input())

if income <= 250000:
    print("No tax")
elif income <= 500000:
    print("5% tax")
elif income <= 1000000:
    print("20% tax")
else:
    print("30% tax")

# 20. 
d = int(input())

if d == 6 or d == 7:
    print("Weekend")
else:
    print("Weekday")

# 21.
gb = int(input())

if gb < 5:
    print("Low usage")
elif gb <= 15:
    print("Medium usage")
else:
    print("High usage")

# 22. 
amt = int(input())

if amt >= 5000:
    print(amt * 0.8)
elif amt >= 2000:
    print(amt * 0.9)
else:
    print(amt)

# 23. 
bmi = float(input())

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

# 24. 
m = int(input())

if m in (3,4,5):
    print("Summer")
elif m in (6,7,8,9):
    print("Rainy")
else:
    print("Winter")

# 25. 
marks = int(input())

if marks >= 40:
    print("Pass")
elif marks >= 35:
    print("Pass with grace")
else:
    print("Fail")

# 26. 
u = input()
p = input()

if u == "admin":
    if p == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")

# 27. 
balance = 5000
amt = int(input())

if amt <= balance and balance - amt >= 1000:
    print("Withdrawal successful")
else:
    print("Transaction failed")

# 28. 
marks = int(input())
test = int(input())

if marks >= 60 and test >= 50:
    print("Eligible")
else:
    print("Not eligible")

# 29. 
a = int(input())
b = int(input())
c = int(input())

if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Equilateral")
    elif a==b or b==c or a==c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid triangle")

# 30. 
marks = int(input())
income = int(input())

if marks >= 80 and income < 200000:
    print("Eligible")
else:
    print("Not eligible")

# 31. 
rating = int(input())
years = int(input())

if rating >= 4 and years >= 5:
    print("Eligible for bonus")
else:
    print("Not eligible")

# 32. 
num = input()

if len(num) == 10 and num[0] in "6789":
    print("Valid mobile number")
else:
    print("Invalid number")

# 33. 
pwd = input()

if len(pwd) >= 8 and any(c.isdigit() for c in pwd):
    print("Strong password")
else:
    print("Weak password")

# 34. 
stock = True
wallet = 2000
price = 1500

if stock and wallet >= price:
    print("Order placed")
else:
    print("Cannot place order")

# 35
fuel = input()

if fuel == "electric" or fuel == "cng":
    print("Vehicle allowed")
else:
    print("Vehicle not allowed")