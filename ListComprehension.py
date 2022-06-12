#Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of a cuboid along with an
# integer N. You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k  is not
# equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z 


from itertools import product
x = [i for i in range(int(input())+1)]
y = [i for i in range(int(input())+1)]
z = [i for i in range(int(input())+1)]
n = int(input())

value = list(product(x,y,z))
require = []
for i in range(len(value)):
    if sum(value[i]) != n:
        require.append(list(value[i]))
print(require)
print(len(require))
#another method is use list comprehension
x = int(input())
y = int(input())
z = int(input())
value = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
print(value)
print(len(value))