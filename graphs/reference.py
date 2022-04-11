import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from random import choice

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


def MNK(x, y, flag=True):
    n = len(x)
    ysr = (np.sum(y) / n)
    xsr = np.sum(x) / n
    y2sr = np.sum(np.square(y)) / n
    ysr2 = ysr ** 2
    x2sr = np.sum(np.square(x)) / n
    xsr2 = xsr ** 2
    yxsr = np.sum(np.multiply(y, x)) / n

    if flag:
        k = (yxsr - ysr * xsr) / (x2sr - xsr2)
        sk = 1 / np.sqrt(n) * np.sqrt((y2sr - ysr2) / (x2sr - xsr2) - k ** 2)
        b = ysr - k * xsr
        sb = sk * np.sqrt(x2sr - xsr2)

    else:
        k = yxsr / x2sr
        sk = np.sqrt((y2sr / x2sr - k ** 2) / n)
        b = 0
        sb = 0

    X = np.arange(0.97 * min(x), 1.03 * max(x))
    print('k = ', k, '+-', sk, '. b = ', b, '+-', sb)
    return X, k, sk, b, sb


def dismiss(V):
    N = len(V)
    M = np.sum(V)/N
    D = 0
    errors = []
    for R in V:
        D += (R-M)**2
    D = np.sqrt(D/N/(N-1))
    return M, D


def graph(x, y, ax, xlbl='', ylbl='', color=(0.2, 0.3, 0.7), s=5, marker='x', label='', flag=True, dismiss_flag=False, dismissx=0, dismissy=0):
    X = np.arange(0, 1.03 * max(x), 0.0001)
    ax.set_ylabel(ylbl)
    ax.set_xlabel(xlbl)
    Y = MNK(x, y, flag)
    dis_x = 0
    dis_y = 0
    if dismiss_flag:
        # dis_y = dismiss(y)[1]
        # dis_x = dismiss(x)[1]
        dis_y = dismissy
        dis_x = dismissx
        ax.errorbar(x, y, xerr=dis_x, yerr=dis_y, fmt='|', color=color, capsize=4, ecolor=color)
    print(dis_x, dis_y)

    k = Y[1]
    b = Y[3]
    ax.scatter(x, y, s=s, marker=marker, color=color)
    ax.plot(X, k * X + b, label=label, color=color)
    if label != '':
        ax.legend(loc='best')
