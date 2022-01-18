import numpy as np
import random
import matplotlib.pyplot as plt


T = 0.8
x = 6
k = [1, -1]
X_Y = range(x)
m = np.zeros((x, x))
for a in range(x):
    for b in range(x):
            m[a, b] = random.choice(k)
s1 = []
s1 = m.copy()
for l in range(301):
    Summa1 = Summa2 = 0
    for c in range(x):
        for d in range(x):
            Summa1 += m[c][d] * m[c][d - 1] + m[c - 1][d] * m[c][d]
    s2 = []
    s2 = m.copy()
    s2[random.choice(X_Y)][random.choice(X_Y)] *= -1
    for e in range(x):
        for f in range(x):
            Summa2 += s2[e][f] * s2[e][f - 1] + s2[e - 1][f] *s2[e][f]  
    delE = Summa2 - Summa1
    if delE <= 0:
        m = s2.copy()
        s1 = m.copy()
    else:
        P = random.uniform(0, 1)
        W = np.exp(-delE/T)
        if P <= W:
            s1 = m.copy()
        else:
            m = s1.copy()





    plt.clf()
    plt.imshow(m)
    plt.draw()
    plt.show()
    plt.gcf().canvas.flush_events()
plt.ioff()
