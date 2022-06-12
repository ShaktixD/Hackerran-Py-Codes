
from collections import Counter


if __name__ == '__main__':
    string = sorted(list(input()))
    x = dict(Counter(string).most_common(3))
    for keys,values in x.items():
        print(keys,values)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
    x,val = Counter(list(input())).most_common(3),()
    for i in range(3):
        val += x[i]
    val = list(val)
    for i in range(0,5,2):
        print(val[i],val[i+1])
        '''