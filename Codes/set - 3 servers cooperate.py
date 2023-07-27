import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

import numpy as num
import math as mathpy
from scipy.optimize import fsolve
from mpl_toolkits.mplot3d import Axes3D

import time

start_time = time.time()
# print("timer started")
mpl.rcParams['lines.linewidth'] = 2


##fig = plt.figure()
##ax = fig.add_subplot(111, projection='3d')

fig = plt.figure()
ax = fig.gca(projection='3d')


eq23list=[]
eq24list=[]
eq25list=[]

Gamma=0.5
#Gamma=float(raw_input("Enter Zipf Factor "))


t=0
AccessCachePrice=[]
ContentIndex=[]
qM=[]
for i in range (1,101,1) :
    t=t + (float(1)/mathpy.pow(i,Gamma))
Omega=float(1)/t
for i in range (1,101,1) :
    q = float(Omega)/ mathpy.pow(i,Gamma)
    #    print q
    qM.append (q)
    AccessCachePrice.append (float(1)/q)
    ContentIndex.append (i)
#    print "qM length is ", len(qM)
qM.append (float(Omega)/ mathpy.pow(101,Gamma))
    #print qM[99]
    #print qM[100]







sigma=0
Pcfinal=0
Posfinal=0
Pafinal=0
NBSproblemfinal=0
NBSproblem=0
Thfinal=0
Thcfinal=0
Pocfinal=0
Poc=Pos=Pc=Pa=0

for Th in range(0,100,10):
    # print(".")
    for Thc in range(Th,100,10):     ###ya range (Th,100,1)
        sigma1=0
        sigma2=0
        for m in range (Th+1,101,1):
            sigma1 += qM[m]
        for m in range (Thc+1,101,1):
            sigma2 += qM[m]
        for Pa in range (0,10,1):
            for Poc in range (0,10,1):
                if(Pa+Poc<10):
                    for Pc in range (0,200,20):
                        for Pos in range (0,200,20):
                            eq23list.append((1-0.1*(Pa+Poc))*(Pa-Th*1-Pc*sigma1))
                            eq24list.append((1-0.1*Poc)*(Pc*sigma1-(Thc-Th)*0.7-Pos*sigma2))
                            eq25list.append((1-0.1*Poc)*(Poc+(Pos-100)*sigma2))
##                            NBSproblem=(eq23)*(eq24)*(eq25)
#                            ax.scatter(eq23, eq24, eq25, c='r', marker='o')
##                            if(NBSproblem>NBSproblemfinal):
##                                NBSproblemfinal = NBSproblem
##                                Thfinal=Th
##                                Thcfinal=Thc
##                                Pcfinal=Pc
##                                Posfinal=Pos
##                                Pafinal=Pa
##                                Pocfinal=Poc






##    plt.scatter(Gamma,Thfinal+5,c='y', marker="s")
##    plt.scatter(Gamma,Thcfinal+10,c='r', marker="p")
##    plt.scatter(Gamma,Pcfinal,c='g', marker="h")       #########   offset to show scatter correctly
##    plt.scatter(Gamma,Posfinal+15,c='b', marker="3")
##    plt.scatter(Gamma,Pafinal+20,c='w', marker="*")
##    plt.scatter(Gamma,Pocfinal+25,c='k', marker=",")
    #    print NBSproblem
    #    print Pc_opt
    #    print("--- %s seconds ---: end of loop on Thc : Th++" % (time.time() - start_time))







# axes = plt.gca()
#
#
# axes.xaxis.set_major_formatter(NullFormatter())
#
# # plt.grid(True)
# axes.axes.get_xaxis().set_ticks([])
# axes.axes.get_yaxis().set_ticks([])
# #axes.axes.get_zaxis().set_ticks([])
# axes.set_zticks([])
# plt.grid(True)
#
# plt.xlabel('First player Utility')
# plt.ylabel('Second player Utility')
# ax.set_zlabel('Third player Utility')
#
# # print '1'
# ax.scatter(eq23list, eq24list, eq25list, c='r', marker='o')


ax = plt.axes(projection='3d')

ax.scatter3D(eq23list, eq24list, eq25list, c=eq25list, cmap='Greens')
plt.xlabel('First player Utility')
plt.ylabel('Second player Utility')
ax.set_zlabel('Third player Utility')




# ax.gride
# ax.w_xaxis.gridlines.set_lw(3.0)
# ax.w_yaxis.gridlines.set_lw(3.0)
# ax.w_zaxis.gridlines.set_lw(3.0)

# tmp_planes = ax.zaxis._PLANES
# ax.xaxis._PLANES = ( tmp_planes[3], tmp_planes[2],
#                      tmp_planes[1], tmp_planes[0],
#                      tmp_planes[5], tmp_planes[4])
#
# ax.yaxis._PLANES = ( tmp_planes[3], tmp_planes[2],
#                      tmp_planes[1], tmp_planes[0],
#                      tmp_planes[5], tmp_planes[4])

#ax.plot(eq23list, eq24list, eq25list, label='parametric curve', marker='o')
#ax.legend()

# print '1'

# ax.view_init(15,45)
# print("--- %s seconds ---:before figure shown" % (time.time() - start_time))
plt.show()



##print "NBSproblemfinal is : ", NBSproblemfinal
##print "Thfinal is : ", Thfinal
##print "Thcfinal is : ", Thcfinal


    ##    NBSproblem = -(mathpy.pow(Pc,2)*mathpy.pow(sigma,2))-(Pc*Th*(1.7)) - (0.7*mathpy.pow(Th,2) )                    #f(Pc,Sigma)
    ##      def func(L5):
    ##          return (float(1)/float(L5+L1))+(float(1)/float(L5+L2+L4))+(float(1)/float(L5+L3+L4))-4
    ##      L5temp = float(fsolve(func, 0.5))







        #find Th from eq 26


        #find Thc from eq 27



        #calculate and report utilities and other stuff


