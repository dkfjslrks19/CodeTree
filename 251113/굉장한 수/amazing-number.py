n = int(input())

print('true' if (n%3==0 and n%2!=0) or (n%2==0 and n%5==0) else 'false')