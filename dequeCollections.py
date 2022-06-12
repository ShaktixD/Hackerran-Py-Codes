from collections import deque
d = deque()
test = int(input())
for i in range(test):
    cmd = input().split()
    if cmd[0] == 'append':
        cmd[1] = int(cmd[1])
        d.append(cmd[1])
    elif cmd[0] == 'pop':
        d.pop()
    elif cmd[0] == 'popleft':
        d.popleft()
    elif cmd[0] == 'appendleft':
        d.appendleft(int(cmd[1]))
    else:
        continue

for i in range(len(d)):
    print(d[i],end =' ')
    
    
'''
A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque 
with approximately the same  performance in either direction.

Click on the link to learn more about deque() methods.
https://docs.python.org/2/library/collections.html#deque-objects

Click on the link to learn more about various approaches to working with deques:
Deque Recipes.

https://docs.python.org/2.7/library/collections.html#deque-recipes
'''