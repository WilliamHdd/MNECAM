import numpy as np
import matplotlib.pyplot as plt

file = '/Users/williamdedecker/Desktop/Informatique/MNECAM/data.txt'
data = np.loadtxt(file)

years = []
EM = []
GE = []
CO = []
for lines in data:
    
    year =  lines[0]
    years.append(year)

    em = lines[1]
    EM.append(em)

    ge = lines[2]
    GE.append(ge)

    co = lines[3]
    CO.append(co)

x = years
y = EM
z = GE
h = CO    
plt.plot(x,y,'o', color ='blue', label = 'EM')
plt.plot(x,z,'o', color = 'red', label = 'GE')
plt.plot(x,h,'o',color = 'green', label = 'CO')
plt.legend(loc = 'best')

plt.show()
