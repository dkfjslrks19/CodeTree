n = int(input())
arr = []
sum = 0

for _ in range(n):
    arr.append(int(input())) #arr = [int(input()) for _ in range(n)]

for i in range(n):
    if arr[i]%2==1 and arr[i]%3==0:
        sum+=arr[i]
print(sum)