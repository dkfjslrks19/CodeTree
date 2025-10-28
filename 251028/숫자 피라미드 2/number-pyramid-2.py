n = int(input())
sum = 1

for i in range(1,n+1):
    for j in range(i):
        print(sum,end=' ')
        sum+=1
    print()