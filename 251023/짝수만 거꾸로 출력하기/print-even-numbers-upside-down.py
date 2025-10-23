n = int(input())
nums = list(map(int, input().split()))

even_num = [x for x in nums if x % 2 == 0]

print(*even_num[::-1])