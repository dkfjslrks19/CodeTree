arr=[]
satisfied = True #3의배수

for _ in range(5):
    arr.append(int(input()))

for i in range(5):
    if arr[i]%3!=0: # 3의 배수가 아니면
        satisfied = False 
        break

if satisfied == False:
    print(0)
else:
    print(1)
