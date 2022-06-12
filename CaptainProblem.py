


'''
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(*[a for a in range(1,i)],*[b for b in range(i+1,0,-1)],sep = '')
'''

from collections import Counter
rep = input()
x = list(map(int,input().split()))
H = dict(Counter(x))
for k,v in H.items():
    if v == 1:
        print(k)