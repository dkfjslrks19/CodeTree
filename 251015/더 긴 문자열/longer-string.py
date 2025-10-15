word = input().split()
word1 = word[0]
word2 = word[1]

if len(word1)>len(word2):
    print('Coding',len(word1))
elif len(word1)<len(word2):
    print('Coding',len(word2))
else:
    print('same')
