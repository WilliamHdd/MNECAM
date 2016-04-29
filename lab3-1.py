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
    
def exo1():
    x = years
    y = EM
    z = GE
    h = CO
    p = np.poly1d(np.polyfit(x,y,2))
    q = np.poly1d(np.polyfit(x,z,2))
    n = np.poly1d(np.polyfit(x,h,2))
    plt.plot(x,y,'o', color ='blue', label = 'EM')
    plt.plot(x,z,'o', color = 'red', label = 'GE')
    plt.plot(x,h,'o',color = 'green', label = 'CO')
    plt.plot(x,p(years),'b--',x,q(years),'r--',x,n(years),'g--')
    plt.legend(loc = 'upper right')
    plt.ylim(0, 170)
    plt.xlim(1999,2017)
    plt.show()

def exo2():
    i = 0
    tot = []
    while i< len(years):
        tot.append(np.sum([EM[i], GE[i], CO[i]]))
        i+=1
    print(tot)
    x = years
    y = tot
    l = np.poly1d(np.polyfit(x,y,1))
    plt.plot(x,l(years))
    o = l(1)
    print(o)
    plt.plot(x,y,'o', label ='Nombres total d etudiants')
    plt.ylim(150,250)
    plt.xlim(1999, 2017)
    plt.legend(loc = 'upper right')
    plt.show()
        


exo2()

