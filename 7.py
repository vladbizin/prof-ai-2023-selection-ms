from sys import stdin, stdout
import numpy as np

E_max=0
n_max=0

N = int(stdin.readline())
for n in range(N):

    k = int(stdin.readline())
    cards = np.array(list(map(int, stdin.readline().split())), dtype='int64')

    nums = np.unique(cards)
    probs = np.bincount(cards)
    probs = probs[probs>0]/k

    less = np.zeros_like(probs)
    less[1:] = np.cumsum(probs)[:-1]

    great = np.zeros_like(probs)
    great[:-1] = np.cumsum(probs[::-1])[::-1][1:]

    gr_eq = np.zeros_like(probs)
    gr_eq[:-1] = np.cumsum((probs**2)[::-1])[::-1][1:]

    l_eq = np.zeros_like(probs)
    l_eq[1:] = np.cumsum((probs**2))[:-1]

    tmp = np.roll(probs, 1)
    tmp1 = np.cumsum(probs[::-1])[::-1] * tmp
    gr_neq = np.cumsum(tmp1[::-1])[::-1]
    gr_neq[:-2] = gr_neq[2:]
    gr_neq[-2:]=0

    tmp = np.roll(probs, -1)
    tmp1 = np.cumsum(probs) * tmp
    l_neq = np.cumsum(tmp1)
    l_neq[2:] = l_neq[:-2]
    l_neq[:2]=0

    p_min = probs**3 + 3 * probs**2 * great + 3 * probs * gr_eq + 6 * probs * gr_neq
    p_max = probs**3 + 3 * probs**2 * less + 3 * probs * l_eq + 6 * probs * l_neq

    E = (nums * (p_min + p_max)).sum()

    if (E > E_max):
        n_max = n
        E_max = E

stdout.write(str(n_max+1) + ' ' + str(E_max))