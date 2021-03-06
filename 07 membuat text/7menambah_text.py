## menambah text

import matplotlib.pyplot as plt
import numpy as np

#membuat plot (sin(2wt + theta))
def sinusGenerator(amplitudo,frekuensi,tAhkhir,theta):
    t = np.arange(0,tAhkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

t,y = sinusGenerator(1,1,4,0)

plt.plot(t,y)

#menambahkan text
#format : plt.text(x,y,'isi text')
plt.text(2,0.5,r'$y = \mathcal{A}.sin(2 \omega t)$')
plt.text(2,0.4,r'$\mathcal{A} = 1 cm, \omega = 1$' + r'$\mathit{hz}$')

plt.show()