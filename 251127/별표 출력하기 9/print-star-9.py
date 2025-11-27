n = int(input())

for i in range(1,n+1): #3
    print('  '*(n-i),end='')
    stars = '* ' * (2*i-1)
    print(stars.rstrip())
    