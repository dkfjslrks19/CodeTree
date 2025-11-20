arr = []
cnt=0

for _ in range(5):
    arr.append(int(input()))

for i in range(5):
    if arr[i]%2==0:
        cnt+=1
print(cnt)