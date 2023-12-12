from sys import stdin, stdout
import numpy as np

T = int(stdin.readline())

for t in range(T):

    n, k = list(map(int, stdin.readline().split()))

    a = np.array(list(map(int, stdin.readline().split())), dtype='ulonglong')

    mat = np.ones((1,n-1))
    for i in range(n-1):
        tmp = np.zeros(n-1)
        tmp[i+1:] = 1
        mat = np.vstack([mat, mat.sum(0) + tmp])
    mat = np.hstack([np.zeros((n,1)), mat])
    mat = mat.astype('ulonglong')

    powers = [1 if k & (1 << (30-_)) else 0 for _ in range(31)][::-1]

    final_mat = np.eye(n, dtype='ulonglong')
    for i, power in enumerate(powers):
        if power==1:
            final_mat = (mat @ final_mat) % 1000000007
        mat = np.linalg.matrix_power(mat, 2) % 1000000007

    a = ((final_mat @ a) % 1000000007).astype('ulonglong')

    stdout.write(' '.join(map(str,a)) + '\n')