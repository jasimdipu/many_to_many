l = [1, 2, 3, 4, 5, 2.5, 4.2, 7.4, "my list", 'mylist2', 10]

# indexing

print(type(l))

print(l[10])

for i in l:
    print(i)

# slicing

print(l[2:5])

print(l[:])

print(l[:-2])

print(l[::-1])

print(l[:] * 2)

l.append(15)
print(l)

# nested list
l2 = [[1, 2, 4], [35, 6, 7]]

print(l2[0][0])

l3 = [10, 20, 30]

for i in l3:
    l.append(i)
print(l)

print(l.count(15))
print('*'*20)
for i in l2:
    for j in i:
        l.append(j)

print(l)

# pop
print(l.pop())
print(l)

pop_val = l.pop(10)
print("poped value", pop_val)
print(l)

# list comprehension
l4 = [i for i in range(1, 100, 10)]
print(l4)

remove_val = l.remove(15)
print(remove_val)
print(l)

l.reverse()
print(l)

l.remove('my list')
l.remove('mylist2')

l.sort()
print(l)
l[0] = 100
print(l)
