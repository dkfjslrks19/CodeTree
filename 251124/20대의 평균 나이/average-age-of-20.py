total = 0
cnt = 0

while True:
    age = int(input())
    if age >=30:
        break
    total += age
    cnt +=1
if cnt > 0:    
    print(f'{total/cnt:.2f}')
