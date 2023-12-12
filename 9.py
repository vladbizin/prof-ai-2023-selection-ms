from sys import stdin, stdout
import numpy as np



n = int(stdin.readline())
m = int(stdin.readline())

A = np.array(list(map(int, stdin.readline().split(','))))
for i in range(1, n):
    A = np.vstack([A, np.array(list(map(int, stdin.readline().split(','))))])

Sum = np.zeros_like(A)
Sum[0,:] = np.cumsum(A[0])

path = np.zeros_like(A)
path[n-1, m-1] = 1
path[0, 0] = 1


for i in range(1, n):
    for j in range(i, m):
        Sum[i,j] = A[i,j] + max(Sum[i-1,j-1], Sum[i,j-1])


i=n-1
j=m-1
while(i!=0):
    if Sum[i, j] == Sum[i-1, j-1] + A[i, j]:
        path[i-1,j-1]=1
        i-=1
        j-=1
    else:
        path[i, j-1]=1
        j-=1

path[0,:j+1] = 1

for row in path:
    stdout.write(', '.join(map(str,row)) + '\n')