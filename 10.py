from sys import stdin, stdout
import numpy as np

n = int(stdin.readline())
m = int(stdin.readline())

X = np.array(list(map(float, stdin.readline().split())))
for i in range(n-1):
    X = np.vstack([X, np.array(list(map(float, stdin.readline().split())))])

p = int(stdin.readline())
q = int(stdin.readline())

W = np.array(list(map(float, stdin.readline().split())))
for i in range(p-1):
    W = np.vstack([W, np.array(list(map(float, stdin.readline().split())))])
W=W.T

grad_wr = np.tile(np.sign(X).sum(0).reshape(-1,1), W.shape[1]).T

grad_xb = np.tile(np.sign(W).sum(1).reshape(-1,1), X.shape[0]).T
approx_deriv = np.zeros_like(X) + np.where(np.logical_and(-1<=X, X<0), (2*X+2), 0) + np.where(np.logical_and(0<=X, X<1), (-2*X+2), 0)
grad_xr = grad_xb * approx_deriv

for row in grad_xr:
    stdout.write(' '.join(map(str,row)) + '\n')

for row in grad_wr:
    stdout.write(' '.join(map(str,row)) + '\n')