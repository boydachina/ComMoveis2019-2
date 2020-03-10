#Aluno: Vítor Gabriel Lemos Lopes
#Projeto de Comunicações Móveis
import matplotlib.pyplot as plt
import numpy as np

freq= [800,1800,1900,2100]
R = 500
dPasso = 50                         # Resolução do grid
dDim = 5*R                          # Dimensão do grid
ht = 32                             # Altura da antena transmissora em metros
hr = 1.5                            # Altura da antena receptora em metros
subR = R*np.sqrt(3)/2               # Curva ortogonal aos lados do Hexágono
ptwa = 37.5                           # Potência de transmissão em Watts inicial


x= np.arange(dPasso,dDim-dPasso,dPasso)
y=np.arange(dPasso,dDim-dPasso,dPasso)
X,Y = np.meshgrid(x,y)

# Matrizes com posição de cada ponto do grid relativa a cada ERB
ERB1 = (X + 1j*Y) - (dDim/2 + (dDim/2)*1j) # Antena central
ERB2 = (X + 1j*Y) - (dDim/2 + 2*subR*1j + (dDim/2)*1j) # Antena central superior
ERB3 = (X + 1j*Y) - (dDim/2 - 2*subR*1j + (dDim/2)*1j) # Antena central inferior
ERB4 = (X + 1j*Y) - (dDim/2 + (R + subR/2) + (subR*1j) + (dDim/2)*1j) # Antena superior direita
ERB5 = (X + 1j*Y) - (dDim/2 + (R + subR/2) - (subR*1j) + (dDim/2)*1j) # Antena inferior direita
ERB6 = (X + 1j*Y) - (dDim/2 - (R + subR/2) + (subR*1j) + (dDim/2)*1j) # Antena superior esquerda
ERB7 = (X + 1j*Y) - (dDim/2 - (R + subR/2) - (subR*1j) + (dDim/2)*1j) # Antena inferior esquerda

ahre = 3.2*(np.log10(11.75*hr))**2 - 4.97 # Fator de correção para cidade grande

def recurs(f,ptw): #função recursiva para ter com maior precisão a potência necessária para ser 2%
    ptdbm = float(10*np.log10(ptw/(10**-3))) # Potência de transmissão em dBm
    
    # Cálculo da potência recebida em cada ponto do grid recebida de cada ERB
    #Modelo Lhata hataurban cost231 para estimativa de perda de percurso
    Lhata1 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB1/1000)) + 3) 
    Lhata2 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB2/1000)) + 3) 
    Lhata3 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB3/1000)) + 3) 
    Lhata4 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB4/1000)) + 3) 
    Lhata5 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB5/1000)) + 3) 
    Lhata6 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB6/1000)) + 3) 
    Lhata7 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB7/1000)) + 3) 
    #Cálculo da melhor potência
    Aux1 = np.maximum(Lhata1,Lhata2)
    Aux2 = np.maximum(Aux1,Lhata3)
    Aux3 = np.maximum(Aux2,Lhata4)
    Aux4 = np.maximum(Aux3,Lhata5)
    Aux5 = np.maximum(Aux4,Lhata6)
    Valor_Maximo = np.maximum(Aux5,Lhata7)

    cont=0 #contador para contar o numero de pontos que foram menores que -90 dBm
    for i in range (len(Valor_Maximo)):
        for j in range (len(Valor_Maximo)):
            if(Valor_Maximo[i,j]<-90):
                cont=cont+1

    perc=100*cont/(len(Valor_Maximo))**2
    if(1.85<perc<=2):
        return ptw
    elif(perc>2):
        return recurs(f,1.3*ptw)
    elif(perc<=1.85):
        return recurs(f,0.8*ptw)
potencia=[]
for frequencia in freq:
    potencia.append(recurs(frequencia,ptwa))
plt.bar(freq,potencia, width=50)
plt.xlabel("Frequência")
plt.ylabel("Potência minima de outage em Watts")
plt.yticks(potencia)
plt.grid()
plt.title("Potência para outage de 2%")
plt.show()