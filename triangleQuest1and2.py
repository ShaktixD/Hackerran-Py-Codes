'''
x = int(input())
for k in range(1,x+1):
    print(*[i for i in range(1,k+1)],*[j for j in range(1,k)][::-1])
'''    

#pro code
'''
for x in range(1,int(input())+1):
    print((((10**x)-1)//9)**2)
'''    
#more shortcut is by the following
#print(*[(((10**j)-1)//9)**2 for j in range(1,int(input())+1)])

#solving traingle quest 1
for i in range(1,int(input())): 
    print((10**(i)//9)*i)