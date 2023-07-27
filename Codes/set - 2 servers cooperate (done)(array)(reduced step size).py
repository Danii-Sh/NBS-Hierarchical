import matplotlib.pyplot as plt
import numpy as num
import math as mathpy
import time
start_time = time.time()
print("Timer started")

U1=[]
U2=[]
scattercount=0
Gamma=0.5
t=0
AccessCachePrice=[]
ContentIndex=[]
qM=[]
for i in range (1,101,1) :
    t=t + (float(1)/mathpy.pow(i,Gamma))
Omega=float(1)/t
for i in range (1,101,1) :
    q = float(Omega)/ mathpy.pow(i,Gamma)
    qM.append (q)
    AccessCachePrice.append (float(1)/q)
    ContentIndex.append (i)
qM.append (float(Omega)/ mathpy.pow(101,Gamma))



x=0
eq26=0
eq26final=1000
Thfinal=0
Pcfinal=0
eq27part1=0
eq27part1final=0
ifinal=0;
for i in range(0,100,1):
    eq26final=1000
    Thfinal=0
    eq27part1=0
    Pc=float(1)/qM[i+1]
    for Th in range(0,100,1):
        eq26=0
        for m in range (Th+1,101,1):
            eq26 += qM[m]
        eq26=Pc*eq26
        eq26 +=Th*1
        if(eq26 < eq26final):
            eq26final = eq26
            Thfinal=Th
    for m in range (Thfinal+1,101,1):
        eq27part1 += qM[m]
    eq27part1=Pc*eq27part1
    eq27part1 += Thfinal*0.7
    if(eq27part1 > eq27part1final):
        eq27part1final = eq27part1
        Pcfinal=Pc
        ifinal=i



##plt.scatter(Gamma,ifinal,c='c', marker="d")

### now Pc and Th are set
Th=ifinal
Pc=Pcfinal

eq24part1=0
for m in range (Th+1,101,1):
    eq24part1 += qM[m]
eq24part1 = eq24part1 *(Pc)
Thcfinal=Posfinal=Pocfinal=sigma2final=xyz=0
eq24x25=0
for Thc in range(Th,100,1):    ## shayad az (Th,100,1)    : X : niaz be eslahe bonyadi be khatere tataboghe Th va Thc

    if(Th>Thc):
        Th=Thc
        Pcfinal=float(1)/qM[Thfinal+1]
        for m in range (Th+1,101,1):
            eq24part1 += qM[m]
        eq24part1 = eq24part1 *(Pc)

    sigma2=0
    for m in range (Thc+1,101,1):
        sigma2 += qM[m]
    for Pos in range (0,200,5):   ## shayad az (100,400,1) ## sarfidan be Co ==> (Co, ta demand,1)  ya (0, ta demand : be khatere coop zarare ye ja ro yeki dige jobran mikone)
##        print "."
        for Poc in num.arange (0,10,0.5):   ### tavajoh be : taghaza nemitune manfi beshe
#            plt.scatter((1-0.1*Poc)*(eq24part1-((Thc-Th)*0.7)-(Pos*sigma2)),(1-0.1*Poc)*(Poc+((Pos-100)*sigma2)),c='y', marker="o")
            U1.append((1-0.1*Poc)*(eq24part1-((Thc-Th)*0.7)-(Pos*sigma2)))
            U2.append((1-0.1*Poc)*(Poc+((Pos-100)*sigma2)))
            scattercount += 1
            eq24x25new= ((1-0.1*Poc)**2)*(eq24part1-((Thc-Th)*0.7)-(Pos*sigma2))*(Poc+((Pos-100)*sigma2))
            if(eq24x25new>eq24x25):
                xyz=(eq24part1-((Thc-Th)*0.7)-(Pos*sigma2))
                eq24x25=eq24x25new
                Thcfinal=Thc
                Posfinal=Pos
                Pocfinal=Poc
                sigma2final=sigma2

##    print "eq24x25 is : ", eq24x25, "Thcfinal is : ",Thcfinal , "xyz is : ",xyz
##    print "Posfinal is : ",Posfinal, "Pocfinal is : ",Pocfinal,"sigma2final is : ",sigma2final

##    plt.scatter(Gamma,Th,c='y', marker="o")
##    plt.scatter(Gamma,Thcfinal,c='g', marker="o")
##    plt.scatter(Gamma,Posfinal,c='b', marker="o")
##    plt.scatter(Gamma,Pocfinal,c='w', marker="o")
##    print ".",int(Gamma*100)   ## namayeshe shomare iteration bare sar naraftane hosele









# axes = plt.gca()
# #axes.axes.get_xaxis().set_visible(False)
# #axes.axes.get_yaxis().set_visible(False)
#
# axes.axes.get_xaxis().set_ticks([])
# axes.axes.get_yaxis().set_ticks([])
#
# plt.scatter(U1,U2)
# #plt.legend(['a','b'])
# plt.xlabel('First Player Utility')
# plt.ylabel('Second Player Utility')
# plt.grid(True)


fig = plt.figure()
ax = fig.gca()
# ax.set_xticks(numpy.arange(0, 1, 0.1))
# ax.set_yticks(numpy.arange(0, 1., 0.1))
plt.xlabel('First Player Utility')
plt.ylabel('Second Player Utility')
plt.scatter(U1, U2)
plt.grid()
plt.show()








##axes.set_xlim([0,1])
##axes.set_ylim([0,400])
print(scattercount)
print("--- %s seconds ---:before figure shown" % (time.time() - start_time))
plt.show()


