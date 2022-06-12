x,y = input(),list(map(int, input().split()))
print(all([z > 0 for z in y]) and any([a == a[::-1] for a in list(map(str,y))]))