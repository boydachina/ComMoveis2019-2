import matplotlib.pyplot as plt
import numpy as np
from fPosUsrSector import fPosUsrSector
from fDrawSector import fDrawSector
from fDrawBs import fDrawBs
def PosGrid():
    vtdR = [50, 100, 500, 2000, 10000]                      # Vetor de raios das celulas em metros
    dR = vtdR[4]                                            # Raio da celula em
    NumUser=1000                                            # Usuários por celula
    vtBs= fDrawBs( dR )                                     #Posição das ERBS
    vtMarkers = ['*','o','d','^','>','+','s']               #Markers para plot
    for ik in range (7): 
        vtPosSector = fPosUsrSector(NumUser, vtBs[ik], dR ) #Posição dos usuarios
        plt.scatter((vtPosSector.real), (vtPosSector.imag),s=5,marker=vtMarkers[ik],label='Sector ERB '+ str(ik+1))
    for iBs in range(1,7):                                           
        fDrawSector(dR,vtBs[iBs])         #Desenhar o hexagono              
        
    plt.legend()  
    plt.title(['7 Células com '+str(NumUser)+' usuários' ])
    plt.xlabel('Distância em m')
    plt.ylabel('Distância em m')
    plt.show()
PosGrid()