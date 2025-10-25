words = ["apple","banana","grape","blueberry","orange"]
ch = input()
count = 0

for w in words:
    if len(w)>=3 and (w[2]==ch or w[3]==ch):
        print(w)
        count+=1
print(count)