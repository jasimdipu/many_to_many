# for, while

for i in range(0, 100, 10):  # 0, n-1
    print(i)

print('*' * 20)

i = 0
n = 10
while i < n:
    print(i)
    i = i + 1
    if i == 100:
        break
