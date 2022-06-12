'''
long beginners descriptable method 

pap = input()
papa = set(map(int,input().split()))
for i in range(int(input())):
    cmd,_ = input().split()
    temp = set(map(int,input().split()))
    if cmd == 'intersection_update':
        papa.intersection_update(temp)
    elif cmd == 'update':
        papa.update(temp)
    elif cmd == 'symmetric_difference_update':
        papa.symmetric_difference_update(temp)
    else:
        papa.difference_update(temp)
    
print(sum(papa))

'''

#RKO's method
pap,papa = input(),set(filter(lambda x: int(x), input().split()))
for i in range(int(input())):
    cmd = input().split()
    temp = set(filter(lambda x: int(x), input().split()))
    eval('papa.'+cmd[0]+'(temp)',{'papa':papa,'temp':temp})
print(sum(list(map(int,papa))))