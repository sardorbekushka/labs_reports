import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font', **{'family': 'Times new roman'})
rc('text', usetex=True)
# rc('text.latex',unicode=True)
rc('text.latex', preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex', preamble=r'\usepackage[russian]{babel}')

fontsize = 15
fig = plt.figure()
# fig.set_figwidth(10)
ax = fig.add_subplot(111)
ax.grid(linestyle='--')


def MNK(x, y):
    n = len(x)
    ysr = (np.sum(y) / n)
    xsr = np.sum(x) / n
    y2sr = np.sum(np.square(y)) / n
    ysr2 = ysr ** 2
    x2sr = np.sum(np.square(x)) / n
    xsr2 = xsr ** 2
    yxsr = np.sum(np.multiply(y, x)) / n

    k = (yxsr - ysr * xsr) / (x2sr - xsr2)

    sk = 1 / np.sqrt(n) * np.sqrt((y2sr - ysr2) / (x2sr - xsr2) - k ** 2)

    b = ysr - k * xsr
    sb = sk * np.sqrt(x2sr - xsr2)
    X = np.arange(0.95 * min(x), 1.05 * max(x))
    print('k = ', k, '+-', sk, '. b = ', b, '+-', sb)
    return X, k, sk, b, sb


def dismiss(V):
    N = len(V)
    M = np.sum(V)/N
    D = 0
    for R in V:
        D += (R-M)**2
    D = np.sqrt(D/N/(N-1))
    return M, D


def graph(x, y, ax, xlbl='', ylbl='', s=5, marker='o', label='', flag=True):
    X = np.arange(0.95 * min(x), 1.05 * max(x))
    ax.set_ylabel(ylbl)
    ax.set_xlabel(xlbl)
    Y = MNK(x, y)
    k = Y[1]
    b = Y[3]
    if flag:
        ax.scatter(x, y, s=s, marker=marker)
        ax.plot(X, k * X + b, label=label)
        if label != '':
            ax.legend(loc='best')



