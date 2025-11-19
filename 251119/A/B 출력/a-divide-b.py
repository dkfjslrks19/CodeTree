A, B = map(int, input().split())

integer_part = A // B
r = A % B

digits = []

for _ in range(20):
    r *= 10
    digits.append(r // B)
    r %= B

print(f"{integer_part}." + ''.join(map(str, digits)))