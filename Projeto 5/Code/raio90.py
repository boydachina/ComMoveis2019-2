import numpy as np
from fUL_sim_Skelenton import fUL_sim_Skelenton
raio=3000#raio de entrada


def recurs(raio):
    usr=200
    rep=100
    x,potr,z=fUL_sim_Skelenton(usr,raio,rep,'teste')
    cont=0 #contador para contar o numero de pontos que foram menores que -121 dBm
    for i in range (len(potr)):
        if(potr[i]<-121):
            cont=cont+1
    #print(raio)
    perc=100*cont/(len(potr))
    #print(perc)
    if(9.95<=perc<10.05):
        return raio
    elif(perc>=10.05):
        return recurs(raio*0.95)
    elif(perc<9.95):
        return recurs(raio*1.05)

raio90=recurs(raio)
print("o tamano do raio para 90% de cobertura:"+ str(raio90) + 'm')