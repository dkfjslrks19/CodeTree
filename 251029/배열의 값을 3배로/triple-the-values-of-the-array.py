array = [list(map(int,input().split())) for _ in range(3)]

for i in range(3):
    for j in range (3):
        array[i][j] *=3
for i in range(3):
    for j in range(3):
        print(array[i][j],end=' ')
    print()