# Enter your code here. Read input from STDIN. Print output to STDOUT

x = list(map(int,input().split()))
print(True if eval(input(),{"x":x[0]})==x[1] else False)