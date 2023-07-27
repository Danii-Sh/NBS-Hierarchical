import matplotlib.pyplot as plt
import numpy as num
import math as mathpy

Thfinalarray = []
Thcfinalarray = []
Gammaarray = []

for Gamma in num.arange(0.01,1.05,0.06):
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
        eq27part1 += Thfinal*0.7     # R = 0.7
        if(eq27part1 > eq27part1final):
            eq27part1final = eq27part1
            Pcfinal=Pc
            ifinal=i

    ##Pc and Th are set
    Thfinal=ifinal
    Pcfinal=Pcfinal
    print(Pcfinal)


##    plt.scatter(Gamma,ifinal,c='c', marker="d")




    Pos_opt=0
    NBSproblemfinal=0
    NBSproblem=0
    Thcfinal=0
    Posfinal=0

    for Thc in range(0,100,1):
        sigma2=0
        for m in range (Thc+1,101,1):
            sigma2 += qM[m]
        x = eq27part1final +((Thfinal-Thc)*0.7)   # x : dar forme : (x-ps)(ps-ys)
        s = sigma2
        y = 100   # = Co

        Pos_opt= ((x*s)-(y*mathpy.pow(s,2)))/(2*mathpy.pow(s,2))
        
        if(Pos_opt > 300):       ## ?????
            Pos_opt=300          ## ?????

        NBSproblem = (x-(Pos_opt*s))*((Pos_opt*s)-(y*s))
        
        if(NBSproblem>NBSproblemfinal):
            NBSproblemfinal = NBSproblem
            Thcfinal=Thc
            Posfinal=Pos_opt
    print ((x-(Pos_opt*s)) , ((Pos_opt*s)-(y*s)))
#    plt.scatter(Gamma,Posfinal,c='b', marker="o")
#    print ("Pos ",Posfinal)
#    print ("1 :: NBS with Pos = 0",(x)*(-(y*s)) ,"NBS with Pos = 100",(x-(10*s))*((10*s)-(y*s)))        
    if(Thfinal>Thcfinal):
        Thfinal=Thcfinal
        Pcfinal=float(1)/qM[Thfinal+1]
        eq27part1final=0
        for m in range (Thfinal+1,101,1):
            eq27part1final += qM[m]
        eq27part1final=Pcfinal*eq27part1final
        eq27part1final += Thc*0.7    # R = 0.7

        x = eq27part1final +((Thfinal-Thcfinal)*0.7)   # x : dar forme : (x-ps)(ps-ys)
        s = sigma2
        y = 100   # = Co

        Posfinal= ((x*s)-(y*mathpy.pow(s,2)))/(2*mathpy.pow(s,2))
 #   print ("2 :: NBS with Pos = 0",(x)*(-(y*s)) ,"NBS with Pos = 100",(x-(10*s))*((10*s)-(y*s))) 
   # plt.scatter(Gamma,Thfinal,c='g', marker="x")
    #plt.scatter(Gamma,Thcfinal,c='r', marker="o")
    Gammaarray.append(Gamma)
    Thfinalarray.append(Thfinal)
    Thcfinalarray.append(Thcfinal)
#    plt.scatter(Gamma,Posfinal,c='g', marker="x")


#########  moshkele Pos : adade ziad : ba rabeteye jadide demand ke neveshtam manfi mishe , pas gereftane meghdare max = 100 ya ... ba tavajoh be B ,a , ...

plt.plot(Gammaarray, Thfinalarray, '-r*', label='Th')
plt.plot(Gammaarray, Thcfinalarray, '-b>', label='Thc')
plt.legend()

axes = plt.gca()
axes.set_xlabel(r'$\gamma$')
axes.set_ylabel('caching threshold')
axes.set_xlim([0,1])
axes.set_ylim([1,100])


plt.show()





