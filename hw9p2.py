
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,.5,1000)

G1=1209*(1/(np.sqrt(2*np.pi)*.0093))*np.exp(-((x-.1182)**2)/(2*(.0093)**2))

G2 = 143*(1 / (np.sqrt(2 * np.pi) * 0.038)) * np.exp(-((x - 0.29) ** 2) / (2 * (0.038 ** 2)))

G3=1066*(1/(np.sqrt(2*np.pi)*.00896))*np.exp(-((x-.0947)**2)/(2*(.00896)**2))

plt.plot(x,G1, label='Peak for p=143/1209')

plt.plot(x,G2, label='Peak for p=42/143')

plt.plot(x,G3,label='Peak for p=101/1066')


plt.xlim(0,.5)


plt.legend()
plt.xlabel('Selection probability')
plt.ylabel('Probabiility density')
plt.title('Distributions for student selection probabilities (scaled)')
plt.show()

#In this code I created the three gausian estimates scaled to their populations size
#These are the plots for the expected probabilty of the three settings, with the 
#STDEV and mean calculated with the binominial expansion formulas. 