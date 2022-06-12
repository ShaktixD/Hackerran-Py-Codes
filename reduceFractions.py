from fractions import Fraction
from functools import reduce

def product(fracs):
    t1 = reduce(lambda x,y : x*y,[i.numerator for i in fracs])
    t2 = reduce(lambda x,y : x*y,[i.denominator for i in fracs])
    results = Fraction(t1,t2)
    return results.numerator,results.denominator
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)