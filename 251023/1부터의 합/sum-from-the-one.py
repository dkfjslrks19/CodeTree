n = int(input())
num = 0

for i in range(1,101):
    num += i
    if num < n:
        continue
    else:
        break
print(i)