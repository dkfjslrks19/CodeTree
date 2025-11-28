n = int(input())

for i in range(1, 2*n + 1):
    if i % 2 == 1:  # 홀수 줄
        stars = i//2 + 1
    else:           # 짝수 줄
        stars = n - i//2 + 1
    
    print("* " * stars)