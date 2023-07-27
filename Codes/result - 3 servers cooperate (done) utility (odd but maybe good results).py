import matplotlib.pyplot as plt
import numpy as num
import matplotlib
import math as mathpy
from scipy.optimize import fsolve
from matplotlib.legend_handler import HandlerLine2D
import time

U1=0
U2=0
U3=0

Usum=[]
Gammalist=[]

Thfinallist=[]
Thcfinallist=[]
Pcfinallist=[]
Posfinallist=[]
Pafinallist=[]
Pocfinallist=[]


matplotlib.use('Qt4Agg')

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

start_time = time.time()
print("timer started")

for Gamma in num.arange(0.01,1.00,0.05):
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



    #Incorrectly Trying to decompose eq 27
    ##sigma=0
    ##Pc=0
    ##eq27part1=0
    ##NBSproblemfinal=0
    ##NBSproblem=0
    ##Thfinal=0
    ##Pcfinal=-200
    ##for Th in range(0,100,1):
    ##    sigma=0
    ##    Pc=0
    ##    NBSproblem=0
    ##    for m in range (Th+1,101,1):   #calculate optimal Pc
    ##        sigma += qM[m]
    ##    Pc=float(-Th*(1.7))/2*sigma         #Pc= f(sigma)
    ##    print "Pc= ",Pc
    ##    NBSproblem = -(mathpy.pow(Pc,2)*mathpy.pow(sigma,2))-(Pc*Th*(1.7)) - (0.7*mathpy.pow(Th,2) )                    #f(Pc,Sigma)
    ##    print "NBSproblem= ",NBSproblem
    ##    if(NBSproblem > NBSproblemfinal):
    ##        NBSproblemfinal = NBSproblem
    ##        Thfinal=Th
    ##        Pcfinal=Pc
    ##print "NBSproblemfinal is : ", NBSproblemfinal
    ##print "Thfinal is : ", Thfinal
    ##print "Pcfinal is : ", Pcfinal






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
                        for Pc in range (0,400,20):
                            for Pos in range (0,300,20):
                                eq23=(1-0.1*(Pa+Poc))*(Pa-Th*1-Pc*sigma1)
                                eq24=(1-0.1*Poc)*(Pc*sigma1-(Thc-Th)*0.7-Pos*sigma2)
                                eq25=(1-0.1*Poc)*(Poc+(Pos-100)*sigma2)
                                NBSproblem=(eq23+100)*(eq24+100)*(eq25+100)
                                if(NBSproblem>NBSproblemfinal):    # and eq23>0 and eq24>0 and eq25>0
                                    NBSproblemfinal = NBSproblem
                                    Thfinal=Th
                                    Thcfinal=Thc
                                    Pcfinal=Pc
                                    Posfinal=Pos
                                    Pafinal=Pa
                                    Pocfinal=Poc

    sigma1=sigma2=0
    for m in range (Thcfinal+1,101,1):
        sigma2 += qM[m]

    for m in range (Thfinal+1,101,1):
        sigma1 += qM[m]

    U1=(((1-0.1*Pocfinal)*((Pcfinal*sigma1)-((Thcfinal-Thfinal)*0.7)-(Posfinal*sigma2))))
    U2=(((1-0.1*Pocfinal)*(Pocfinal+((Posfinal-100)*sigma2))))
    U3=((1-0.1*(Pafinal+Pocfinal))*(Pafinal-Thfinal*1-Pcfinal*sigma1))
    Usum.append(U1+U2+U3)
    Gammalist.append(Gamma)


	


 
    Thfinallist.append(Thfinal)
    Thcfinallist.append(Thcfinal)
    Pcfinallist.append(Pcfinal)
    Posfinallist.append(Posfinal)
    Pafinallist.append(Pafinal)
    Pocfinallist.append(Pocfinal)
               
#    plt.scatter(Gamma,Thfinal,c='y', marker="s")
#    plt.scatter(Gamma,Thcfinal,c='r', marker="p")
#    plt.scatter(Gamma,Pcfinal,c='g', marker="D")       #########   offset to show scatter correctly
#    plt.scatter(Gamma,Posfinal,c='b', marker="3")
#    plt.scatter(Gamma,Pafinal,c='w', marker="*")
#    plt.scatter(Gamma,Pocfinal,c='k', marker=",")

    #    print NBSproblem
    #    print Pc_opt 
    #    print("--- %s seconds ---: end of loop on Thc : Th++" % (time.time() - start_time))
    print(".", float(Gamma*100))

print("Gammalist length ",len(Gammalist))
print("Usum length ",len(Usum))

lns1 = ax1.plot(Gammalist, Thfinallist , '-r', marker='x', label='red star')
lns2 = ax1.plot(Gammalist, Thcfinallist , '-y', marker='>', label='yellow')
lns3 = ax2.plot(Gammalist, Pcfinallist , '-g', marker='<', label='green')
lns4 = ax2.plot(Gammalist, Posfinallist , '-b', marker='D', label='blue')
lns5 = ax2.plot(Gammalist, Pafinallist , '-c', marker='D', label='cyen')
lns6 = ax2.plot(Gammalist, Pocfinallist , '-k', marker='p', label='black')

lns = lns1+lns2+lns3 + lns4+lns5+lns6
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=10, fontsize=10)
#plt.legend(handler_map={lns: HandlerLine2D(numpoints=4)})

#ax1.grid()

#plt.scatter(Gammalist,Usum,c='k', marker=",")
axes = plt.gca()
axes.set_xlim([0,0.951])
#axes.set_ylim([0,200])

ax1.set_ylim([0,100])
ax2.set_ylim([0,400])

ax1.set_xlabel(r'$\gamma$')
ax1.set_ylabel('caching threshold')
ax2.set_ylabel('price')

print("--- %s seconds ---:before figure shown" % (time.time() - start_time))
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
