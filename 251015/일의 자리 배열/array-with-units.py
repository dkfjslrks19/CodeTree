a, b = map(int,input().split())
a, b < 10

seq = [a,b]
for i in range(2,10):
    next_num = (seq[i-2]+seq[i-1])%10
    seq.append(next_num)
print(*seq)

