n = int(input())

for i in range(n):
    print("  " * i, end="")        # 공백 2칸
    stars = "* " * (2*(n - i) - 1) # 별 + 공백
    print(stars.rstrip())