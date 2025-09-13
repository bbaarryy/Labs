import math

def get_ab(i20,u20):
    x_a,y_a,xy_a,x2_a =0,0,0,0
    y2_a = 0
    r_a = 0
    for i in range(len(i20)):
        x_a += i20[i]
        y_a += u20[i]
        xy_a += i20[i] * u20[i]
        x2_a += i20[i] ** 2
        y2_a += u20[i] **2
        r_a += 5000*u20[i]/(i20[i]*5000 - u20[i])
    xy_a /= 10
    x_a /=10
    y_a /=10
    x2_a /=10
    y2_a /=10

    #print(xy_a/x2_a,r_a/10)
    #print(y2_a,x2_a)
    
    b = xy_a/x2_a
    print(y2_a,x2_a,b)
    print((1/(math.sqrt(10))) * (math.sqrt(y2_a/x2_a - b*b)))
    
    #print(xy_a/x2_a)

import numpy as np
import matplotlib.pyplot as plt

i20 = [363,228,126.8,94.2,78.5,59,50.5,31.2,26.8,24.4]
u20 = [720,450,250,185,150,115,95,55,50,45]

i30 = [240.7,150.7,93.4,80.1,66,54,35,28.5,21.8,42.5]
u30 = [715,450,275,235,190,155,100,80,60,120]

i50 = [144.7,102.7,118.6,73.4,59,47.2,30.3,26,27.5,22.2]
u50 = [720,510,590,360,290,230,145,125,135,105]

get_ab(i20,u20)
# get_ab(i30,u30)
# get_ab(i50,u50)

err_i = [0.01]
err_u = [1.25]

plt.figure(figsize=(20,20))
plt.errorbar(i20,u20,xerr=err_i,yerr = err_u,ls='',capsize = 5)
plt.errorbar(i30,u30,xerr=err_i,yerr = err_u,ls='',capsize = 5)
plt.errorbar(i50,u50,xerr=err_i,yerr = err_u,ls='',capsize = 5)

x1 = np.linspace(0, 400, 10)
y = 2*x1 - 4.6
plt.plot(x1,y)

x2 = np.linspace(0, 250, 10)
y2 = 3*x2-6
plt.plot(x2,y2)

x3 = np.linspace(0, 150, 10)
y3 = 5*x3 - 5.9
plt.plot(x3,y3)

plt.xlabel("I, mA") # Подпись оси X
plt.ylabel("U, mV") # Подпись оси Y
plt.grid()
#plt.show()
#print(1)