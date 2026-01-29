# 1. Print all digits of a number
n = int(input("Enter number: "))

while n > 0:
    d = n % 10
    print(d)
    n //= 10

# 2. Sum of digits
n = int(input("Enter number: "))
s = 0

while n > 0:
    s += n % 10
    n //= 10

print("Sum =", s)

# 3. Count digits
n = int(input("Enter number: "))
c = 0

while n > 0:
    c += 1
    n //= 10

print("Digits =", c)

# 4. Reverse a number
n = int(input("Enter number: "))
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print("Reverse =", rev)

# 5. Palindrome check
n = int(input("Enter number: "))
t = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if rev == t:
    print("Palindrome")
else:
    print("Not Palindrome")

# 6. Product of digits
n = int(input("Enter number: "))
p = 1

while n > 0:
    p *= n % 10
    n //= 10

print("Product =", p)

# 7. Largest digit
n = int(input("Enter number: "))
mx = 0

while n > 0:
    d = n % 10
    if d > mx:
        mx = d
    n //= 10

print("Largest digit =", mx)

# 8. Smallest digit
n = int(input("Enter number: "))
mn = 9

while n > 0:
    d = n % 10
    if d < mn:
        mn = d
    n //= 10

print("Smallest digit =", mn)

# 9. Armstrong number
n = int(input("Enter number: "))
t = n
s = 0

while n > 0:
    d = n % 10
    s += d ** 3
    n //= 10

if s == t:
    print("Armstrong number")
else:
    print("Not Armstrong")

# 10. Remove all zeros
n = int(input("Enter number: "))
res = 0
p = 1

while n > 0:
    d = n % 10
    if d != 0:
        res = d * p + res
        p *= 10
    n //= 10

print("Without zeros =", res)

# 11. Count even and odd digits
n = int(input("Enter number: "))
even = 0
odd = 0

while n > 0:
    d = n % 10
    if d % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10

print("Even digits:", even)
print("Odd digits:", odd)

# 12. Check specific digit (5)
n = int(input("Enter number: "))
found = False

while n > 0:
    if n % 10 == 5:
        found = True
        break
    n //= 10

if found:
    print("Digit 5 found")
else:
    print("Digit 5 not found")

# 13. Sum of even and odd digits
n = int(input("Enter number: "))
se = 0
so = 0

while n > 0:
    d = n % 10
    if d % 2 == 0:
        se += d
    else:
        so += d
    n //= 10

print("Sum of even digits:", se)
print("Sum of odd digits:", so)

# 14. Square each digit
n = int(input("Enter number: "))
res = 0
p = 1

while n > 0:
    d = n % 10
    res = (d*d) * p + res
    p *= 100
    n //= 10

print("New number =", res)

# 15. Perfect number
n = int(input("Enter number: "))
s = 0
i = 1

while i < n:
    if n % i == 0:
        s += i
    i += 1

if s == n:
    print("Perfect number")
else:
    print("Not perfect")

# 16. Fibonacci series
n = int(input("Enter terms: "))
a = 0
b = 1
i = 1

while i <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    i += 1

# 17. Factorial
n = int(input("Enter number: "))
f = 1

while n > 0:
    f *= n
    n -= 1

print("Factorial =", f)

# 18. Power (a^b)
a = int(input("Enter base: "))
b = int(input("Enter power: "))
p = 1

while b > 0:
    p *= a
    b -= 1

print("Result =", p)

# 19. GCD
a = int(input("Enter a: "))
b = int(input("Enter b: "))

while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print("GCD =", a)

# 20. Prime number
n= 7 
factor = 0
i = 1
while i<= n :
    if n% i == 0 :
        factor += 1 
    i += 1
if factor == 2 :
    print('prime number')
else:
    print('not a prime number')    
