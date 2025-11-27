n = int(input())

for i in range(n):
    stars = n - i          # 양쪽 별 개수
    spaces = 2 * i         # 가운데 공백 개수
    
    print('*' * stars + ' ' * spaces + '*' * stars)