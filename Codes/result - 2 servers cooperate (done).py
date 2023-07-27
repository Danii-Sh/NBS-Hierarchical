import matplotlib.pyplot as plt
import numpy as num
import math as mathpy
import time
start_time = time.time()
print("Timer started")

Thlist=[]
Gammalist=[]

Thclist=[]
Poslist=[]
Poclist=[]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

for Gamma in num.arange(0.01,1.06,0.06):
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



    #plt.scatter(Gamma,ifinal,c='c', marker="d")

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
        for Pos in range (0,300,1):   ## shayad az (100,400,1) ## sarfidan be Co ==> (Co, ta demand,1)  ya (0, ta demand : be khatere coop zarare ye ja ro yeki dige jobran mikone)
            for Poc in num.arange (0,10,0.5):   ### tavajoh be : taghaza nemitune manfi beshe

                eq24x25new= ((1-0.1*Poc)**2)*(eq24part1-((Thc-Th)*0.7)-(Pos*sigma2))*(Poc+((Pos-100)*sigma2))

                if(eq24x25new>eq24x25):
                    xyz=(eq24part1-((Thc-Th)*0.7)-(Pos*sigma2))
                    eq24x25=eq24x25new
                    Thcfinal=Thc
                    Posfinal=Pos
                    Pocfinal=Poc
                    sigma2final=sigma2
    print ( (eq24part1-((Thcfinal-Th)*0.7)-(Posfinal*sigma2final)) , (Pocfinal+((Posfinal-100)*sigma2final) ))
                
##    print "eq24x25 is : ", eq24x25, "Thcfinal is : ",Thcfinal , "xyz is : ",xyz
##    print "Posfinal is : ",Posfinal, "Pocfinal is : ",Pocfinal,"sigma2final is : ",sigma2final
    Thlist.append(Th)
    Gammalist.append(Gamma)
#    plt.plot(Gamma,Th,'.r-')
#    plt.plot(Gamma,Thcfinal,c='g', marker="o")
#    plt.plot(Gamma,Posfinal,c='b', marker="o")
#    plt.plot(Gamma,Pocfinal,c='r', marker="o")
    Thclist.append(Thcfinal)
    Poslist.append(Posfinal)
    Poclist.append(Pocfinal)



    print("#",int(Gamma*100))   ## namayeshe shomare iteration bare sar naraftane hosele


ln1 = ax1.plot(Gammalist,Thlist,'-r>', label='Th', markeredgewidth=3, markeredgecolor='k')
ln2 = ax1.plot(Gammalist,Thclist,'-gD', label='Thc', markeredgewidth=3, markeredgecolor='k')
ln3 = ax2.plot(Gammalist,Poslist,'-cp', label='Pos',  markeredgewidth=3, markeredgecolor='maroon')
ln4 = ax2.plot(Gammalist,Poclist,'-bx', label='Poc',  markeredgewidth=3, markeredgecolor='maroon')
ln = ln1+ln2+ln3+ln4
labs = [l.get_label() for l in ln]
ax1.legend(ln, labs, loc=0)


axes = plt.gca()
ax1.set_xlim([0,1])
ax1.set_ylim([0,150])

ax2.set_ylim([0,350])
ax1.set_xlabel(r'$\gamma$')
ax1.set_ylabel('caching threshold', color='k')
ax2.set_ylabel('price', color='maroon')

print("--- %s seconds ---:before figure shown" % (time.time() - start_time))
plt.show()





