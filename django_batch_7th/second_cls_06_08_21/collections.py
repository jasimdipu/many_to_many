# list, tuple, set, dictionary

# list -> mutable collection
l = [1, 2, 3, 4.5, 5.5, 6.5, '7.5', '8.5', '9.5', "name", 'age', True, False]

l[0] = 100

# print(type(l))
print(l)
# for i in l:
#     print(i)
#     print(type(i))

# tuple -> immutable collection
t = (1, 2, 3, 4.5, 5.5, 6.5, '7.5', '8.5', '9.5', "name", 'age', True, False)
# t[0] = 100 #cause of immutable
# print(type(t))
print(t)
# for i in t:
#     print(i)
#     print(type(i))

# set -> immutable
s = {1, 2, 3, 4, 5}
print(s)
# s[0] = 100

# dictionary -> key: value pair
d = {"key1": "value1", "key2": "value2", 'key3': 'value3'}
d2 = {0: 10, 1: 20, 2: 30}
print(d2[0])
