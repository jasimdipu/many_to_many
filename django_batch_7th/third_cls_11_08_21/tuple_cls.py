t = (1, 2, 3, 54, 6, 45, 32, 4, 6, 65, 75, 2, 4, 4, 6)
# indexing

print(type(t))

print(t[10])

for i in t:
    print(i)

# sticing

print(t[2:5])

print(t[:])

print(t[:-2])

print(t[::-1])

print(t[:] * 2)

# immutable
# t[0] = 100
# print(t)

print(t.count(2))
print(t.index(2))

for i in t:
    if i == 2:
        continue
    indx = t.index(i)
    print(indx)

