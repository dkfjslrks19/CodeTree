n = int(input())

for i in range(n):
    restars = '* ' * (n-i)
    stars = '* ' * (i+1)
    print(restars)
    print(stars)