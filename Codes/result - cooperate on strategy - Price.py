import matplotlib.pyplot as plt
import numpy as num
import math as mathpy

eq23=0
eq30=0

Gammaarray = []
Pafinalarray = []
Pocfinalarray = []

u1=[]
u2=[]

for Gamma in num.arange(0.01,1.05,0.05):
##Gamma=float(raw_input("Enter Zipf Factor "))
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
        eq27part1 += Thfinal*0.7   #  R = 0.7 
        if(eq27part1 > eq27part1final):
            eq27part1final = eq27part1
            Pcfinal=Pc
            ifinal=i

    ##Pc and Th are set
    Thfinal=ifinal
    Pcfinal=Pcfinal
    print(Pcfinal)
##    plt.scatter(Gamma,ifinal,c='r', marker="o") 
##    print "Pc is ",Pcfinal

    x=0
    eq28=0
    eq28final=-1000
    Thcfinal=0
    Posfinal=0
    eq27part2=0
    eq27part2final=-1000
    ifinal=0;
    for i in range(0,100,1):
        eq28=0
        Thcfinal=0
        eq27part2final=-1000
        Pos=float(0.7)/qM[i+1]
        for Thc in range(0,100,1):
            eq27part2=0
            for m in range (Thc+1,101,1):
                eq27part2 += qM[m]
            eq27part2=Pos*eq27part2
            eq27part2 +=Thc*0.7
            eq27part2 = -eq27part2
            
            if(eq27part2 > eq27part2final):
                eq27part2final = eq27part2
                Thcfinal=Thc
        for m in range (Thcfinal+1,101,1):
            eq28 += qM[m]
        eq28=(Pos-100)*eq28    #  Co = 100 
        if(eq28 > eq28final):
            eq28final = eq28
            Posfinal=Pos
            ifinal=i

    ##Pos and Thc are set


    Thcfinal=ifinal
##    print Thcfinal,Thfinal
    Posfinal=Posfinal
##    plt.scatter(Gamma,ifinal,c='c', marker="d")


    if (Thfinal>Thcfinal):
        Thfinal=Thcfinal
        Pcfinal=float(1)/qM[Thfinal+1]

    eq29x30=-1000
    Pocfinal=Pafinal=0

    for Pa in range (0,11,1):   ## shayad az (100,400,1)
        for Poc in range (0,11,1):   ### tavajoh be : taghaza nemitune manfi beshe
            if(Poc+Pa)<10:
                eq29x30new= ((eq28final+Poc)*(1-(0.1*Poc))+100)*((Pa-eq27part1final)*(1-(0.1*Poc)-(0.1*Pa))+100)
                u1.append( (eq28final+Poc)*(1-(0.1*Poc)))
                u2.append((Pa-eq27part1final)*(1-(0.1*Poc)-(0.1*Pa)))
                if(eq29x30new>eq29x30):
                    eq29= (eq28final+Poc)*(1-(0.1*Poc))
                    eq30=(Pa-eq27part1final)*(1-(0.1*Poc)-(0.1*Pa))
                    eq29x30=eq29x30new
                    Pocfinal=Poc
                    Pafinal=Pa
 ##   plt.scatter(Gamma,Pafinal,c='g', marker="o")
 ##  plt.scatter(Gamma,Pocfinal,c='b', marker="x")
    
    Gammaarray.append(Gamma)
    Pafinalarray.append(Pafinal)
    Pocfinalarray.append(Pocfinal)

    print(".",Gamma*100 , "Pa = ",Pafinal, "eq 29 and eq 30: utilities",eq29,eq30)
    eq29=0
    eq30=0
##print "Thfinal ",Thfinal,"Pcfinal ",Pcfinal
##print "Thcfinal ",Thcfinal,"Posfinal ",Posfinal
##print "Pocfinal ",Pocfinal,"Pafinal ",Pafinal

#plt.scatter(u1,u2,c='r', marker ="o")

plt.plot(Gammaarray, Pafinalarray, '-r*', label='Pa')
plt.plot(Gammaarray, Pocfinalarray, '-b>', label='Poc')

#plt.plot(Gammaarray, Pafinalarray, '-r*', label='Pa', markevery=3)
#plt.plot(Gammaarray, Pocfinalarray, '-b>', label='Poc', markevery=3)

plt.legend()

axes = plt.gca()
axes.set_xlabel(r'$\gamma$')
axes.set_ylabel('Price')
axes.set_xlim([0,1])
#axes.set_ylim([0,15])

#axes = plt.gca()
#axes.set_xlim([0,1])
#axes.set_ylim([0,15])


plt.show()
