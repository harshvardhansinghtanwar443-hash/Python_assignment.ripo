# question-1
li =[1,2,3,4]
print(li)

#question - 2
li = [1,'harsh',7.5]
for i in range(len(li)):
    print(type(li[i]), li[i])

#question-3
li = [1,2,3,4]
print(len(li))

#question - 4
li=[]
li1 = [1,2,3]
li.extend(li1)
print(li)

# list indexing 
# question - 1
li = [1,2,3,4,5,6]
print(li[0])

#2
li = [1,2,3,4,5,6]
print(li[-1])

#3
li = [1,2,3,4,5,6]
print(li[2])

#4
li = [1,2,3,4,5,6]
print(li[0:3])

#5
li = [1,2,3,4,5,6]
print(li[-6::1])

#list mutablity 
#1
li = [1,2,3,4,5,6]
li.pop(1)
li.insert(1,7)
print(li)

#2
li = [1,2,3,4,5,6]
li.pop(5)
li.insert(5,100)
print(li)

#3
li = [1,2,3,4,5,6]

# List Methods (append, extend, insert)
li = [1,2,3,4,5,6]
li.append(7)
print(li)

#2
li = [1,2,3,4,5,6]
li1 = [7,8,9]
li.extend(li1)
print(li)

#3

li = [1,2,3,4,5,6]
li.pop(5)
li.insert(5,100)
print(li)

#Removing Elements
#1
li = [1,2,3,4,5,6]
li.remove(2)
print(li)

#2
li = [1,2,3,4,5,6]
li.pop(3)
print(li)

#3
li = [1,2,3,4,5,6]
li.clear()
print(li)

# Loop with List
li = [1,2,3,4,5,6]
for el in li :
    print(el,end=' ')
print()
# 2
li = [1,2,3,4,5,6]
for el in li :
    if el % 2 == 0 :
        print('even',el,end=',')
    else:
        print('odd',el,end=',')
print()

# 3
li = [1,2,11,13,15]
max = 0
for a in li:
    if a > 10 :
        max += 1
print(max,'are graeter the 10')

li = [1,2,3,4,5,6]
sum = 0
for i in range (len(li)):
    sum += li[i]
print(sum)

    

