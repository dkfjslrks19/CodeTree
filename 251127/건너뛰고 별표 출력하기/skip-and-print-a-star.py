n = int(input()) #5

for i in range(1,n+1): #1~5
    for j in range(i):
        print('*',end='')
    print()
    print()

for i in range(n-1,0,-1): #6부터 시작 
    for j in range(i):
        print('*',end='')
    print()
    print()