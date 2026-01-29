# 1 . while loop to print all digits of a number one by one
# n = 1234
# i = 0
# while n > 0:
#     digit = n % 10
#     print(digit,end=',')
#     n = n //10

#2.sum of all digit 
# n = 1234
# i = 0 
# while n> 0 :
#     digit = n % 10
#     i = i+ digit
#     print(i)
#     n = n // 10

# 3.digit count 
# n = 1234
# i = 0
# while n > 0 :
#     digit =  n % 10
#     i += 1
#     n = n // 10
# print(i)

# 4. reversing a number
# a = 1234
# i = 0
# while a > 0 :
#     digit = a % 10
#     print(digit,end='')
#     a = a// 10

#5.palindrom 
# n = 121 
# org = n 
# digit = 0 
# while n > 0:
#     digit = digit* 10 + n%10 
#     n = n // 10
# if org == digit :
#     print('palindrom')
# else:
#     print('not palindrom')

#6.product of digits 
# n = 1234
# i = 1
# while n > 0 :
#     d = n % 10
#     i *= d 
#     n = n // 10
# print(i)

#7.largest digit 
# n = 1234
# i = 0 
# while n > 0 :
#     d = n % 10 
#     if d > i :
#         i = d 
#     n = n //10
# print('largest didgit',i)

# 8 . smallest digit 
# n = 1234
# i = 9 
# while n > 0 :
#     d =  n % 10
#     if d < i:
#         i = d
#     n = n // 10
# print('minimum digit',i)

# 9 . armstrong number
# n = int(input('enter your num : '))
# sum = 0
# temp = n
# while n > 0 :
#     d = n % 10 
#     sum = sum + d ** 3
#     n = n // 10
# if temp == sum :
#     print('armstrong number')
# else:
#     print('not')

 # 10 to remove zero 
n = int(input('enter your num : '))
new = 0 
place = 1
while n > 0 :
    d = n % 10
    if d != 0 :
        new = new +d * place
        place *= 10
    n = n // 10
print(new)    

