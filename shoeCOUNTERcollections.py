# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
x = int(input())
sizes = input().split()
sizes = list(map(int,sizes))
customers = int(input())
earnings = 0
for i in range(customers):
    target = input().split()
    target = list(map(int,target))
    if target[0] in sizes:
        sizes.remove(target[0])
        earnings +=target[1]
    else:
        continue
print(earnings)

"""
#=======================================================
"""
using another method
"""
from collections import Counter

x = int(input())
sizes = input().split()
sizes = Counter(list(map(int,sizes)))
customers = int(input())
earnings = 0

for i in range(customers):
    target = input().split()
    target = list(map(int,target))
    if sizes[target[0]] != 0:
        earnings += target[1]
        if sizes[target[0]] >0:
            sizes[target[0]] -=1

print(earnings)