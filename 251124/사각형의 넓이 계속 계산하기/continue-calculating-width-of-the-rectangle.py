while True:
    w,h,ch = input().split()
    w = int(w)
    h = int(h)

    area = w * h
    print(area)

    if ch == 'C':
        break