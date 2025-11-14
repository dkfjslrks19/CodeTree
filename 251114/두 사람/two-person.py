a_age,b = input().split()
c_age,d = input().split()
a = int(a_age)
c = int(c_age)

if (a>=19 and b=='M') or (c>=19 and d=='M'):
    print(1)
else:
    print(0)

