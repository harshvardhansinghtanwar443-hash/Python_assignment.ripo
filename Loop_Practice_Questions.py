# 1. Print numbers from 1 to 50
for i in range(1, 51):
    print(i)

# 2. Print numbers from 50 to 1
for i in range(50, 0, -1):
    print(i)

# 3. Print all even numbers between 1 and 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# 4. Print all odd numbers between 1 and 100
for i in range(1, 101):
    if i % 2 != 0:
        print(i)

# 5. Print numbers from 10 to 100 with step 10
for i in range(10, 101, 10):
    print(i)

# 6. Print square of numbers from 1 to 10
for i in range(1, 11):
    print(i * i)

# 7. Print cube of numbers from 1 to 5
for i in range(1, 6):
    print(i * i * i)

# 8. Sum of numbers from 1 to 100
s = 0
for i in range(1, 101):
    s += i
print(s)

# 9. Table of 9
for i in range(1, 11):
    print(9 * i)

# 10. Numbers 1 to 30, skip multiples of 4
for i in range(1, 31):
    if i % 4 == 0:
        continue
    print(i)

# 11. Stop when number becomes 25
for i in range(1, 51):
    if i == 25:
        break
    print(i)

# 12. Stop at first number divisible by 7
for i in range(1, 101):
    if i % 7 == 0:
        break
    print(i)

# 13. Skip numbers divisible by 5
for i in range(1, 41):
    if i % 5 == 0:
        continue
    print(i)

# 14. Print 10 to 1, stop at 4
for i in range(10, 0, -1):
    if i == 4:
        break
    print(i)

# 15. Skip numbers between 30 and 40
for i in range(1, 101):
    if i >= 30 and i <= 40:
        continue
    print(i)

# 16. Stop when number ends with 7
for i in range(1, 101):
    if i % 10 == 7:
        break
    print(i)

# 17. Print only odd numbers
for i in range(1, 51):
    if i % 2 != 0:
        print(i)

# 18. Stop when divisible by 3 and 5
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        break
    print(i)

# 19. Skip multiples of 6
for i in range(1, 61):
    if i % 6 == 0:
        continue
    print(i)

# 20. 100 to 1, stop at 55
for i in range(100, 0, -1):
    if i == 55:
        break
    print(i)

# 21. Skip numbers between 10 and 20
for i in range(1, 31):
    if i >= 10 and i <= 20:
        continue
    print(i)

# 22. Stop when sum crosses 200
s = 0
for i in range(1, 101):
    s += i
    if s > 200:
        break
    print(i)

# 23. Skip numbers ending with 3
for i in range(1, 51):
    if i % 10 == 3:
        continue
    print(i)

# 24. Stop at first even number > 50
for i in range(1, 101):
    if i > 50 and i % 2 == 0:
        break
    print(i)

# 25. Skip numbers divisible by both 2 and 3
for i in range(1, 41):
    if i % 2 == 0 and i % 3 == 0:
        continue
    print(i)


# 26. Print 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# 27. Print 20 to 1
i = 20
while i >= 1:
    print(i)
    i -= 1

# 28. Even numbers 1 to 50
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1

# 29. Odd numbers 1 to 50
i = 1
while i <= 50:
    if i % 2 != 0:
        print(i)
    i += 1

# 30. Table of 5
i = 1
while i <= 10:
    print(5 * i)
    i += 1

# 31. Sum 1 to 100
i = 1
s = 0
while i <= 100:
    s += i
    i += 1
print(s)

# 32. 10 to 100 step 10
i = 10
while i <= 100:
    print(i)
    i += 10

# 33. Square 1 to 10
i = 1
while i <= 10:
    print(i * i)
    i += 1

# 34. Count 1 to 30
i = 1
while i <= 30:
    print(i)
    i += 1

# 35. 100 to 0 step -5
i = 100
while i >= 0:
    print(i)
    i -= 5

# 36. Multiples of 7 (1–100)
i = 1
while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1

# 37. Product of 1 to 10
i = 1
p = 1
while i <= 10:
    p *= i
    i += 1
print(p)

# 38. Skip multiples of 4
i = 1
while i <= 50:
    if i % 4 != 0:
        print(i)
    i += 1

# 39. Stop at 60
i = 1
while i <= 100:
    if i == 60:
        break
    print(i)
    i += 1

# 40. Stop when number ends with 9
i = 1
while i <= 40:
    if i % 10 == 9:
        break
    print(i)
    i += 1


