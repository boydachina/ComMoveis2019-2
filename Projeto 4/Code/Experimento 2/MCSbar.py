import numpy as np
import matplotlib.pyplot as plt
import math
def QMCS(snre):
    mcs=np.zeros(29)
    for i in range(len(snre)):
        if(snre[i]<-6.7):continue
        if(snre[i]<=-4.7)and(snre[i]>=-6.7):mcs[0]+=1
        if(snre[i]>-4.7)and(snre[i]<=-2.3):mcs[1]+=1
        if(snre[i]>-2.3)and(snre[i]<=-2.3-(-2.3-0.2)/2):mcs[2]+=1     
        if(snre[i]>-2.3-(-2.3-0.2)/2)and(snre[i]<=0.2):mcs[3]+=1
        if(snre[i]>0.2)and(snre[i]<=0.2-(0.2-2.4)/2):mcs[4]+=1
        if(snre[i]>0.2-(0.2-2.4)/2)and(snre[i]<=2.4):mcs[5]+=1
        if(snre[i]>2.4)and(snre[i]<=2.4-(2.4-4.3)/2):mcs[6]+=1
        if(snre[i]>2.4-(2.4-4.3)/2)and(snre[i]<=4.3):mcs[7]+=1      
        if(snre[i]>4.3)and(snre[i]<=4.3-(4.3-5.9)/3):mcs[8]+=1
        if(snre[i]>4.3-(4.3-5.9)/3)and(snre[i]<=4.3-(4.3-5.9)*2/3):mcs[9]+=1
        if(snre[i]>4.3-(4.3-5.9)*2/3)and(snre[i]<=5.9):mcs[10]+=1
        if(snre[i]>5.9)and(snre[i]<=5.9-(5.9-8.1)/2):mcs[11]+=1
        if(snre[i]>5.9-(5.9-8.1)/2)and(snre[i]<=8.1):mcs[12]+=1
        if(snre[i]>8.1)and(snre[i]<=8.1-(8.1-10.3)/2):mcs[13]+=1
        if(snre[i]>8.1-(8.1-10.3)/2)and(snre[i]<=10.3):mcs[14]+=1
        if(snre[i]>10.3)and(snre[i]<=10.3-(10.3-11.7)/3):mcs[15]+=1
        if(snre[i]>10.3-(10.3-11.7)/3)and(snre[i]<=10.3-(10.3-11.7)*2/3):mcs[16]+=1 
        if(snre[i]>10.3-(10.3-11.7)*2/3)and(snre[i]<=11.7):mcs[17]+=1
        if(snre[i]>11.7)and(snre[i]<=11.7-(11.7-14.1)/2):mcs[18]+=1
        if(snre[i]>11.7-(11.7-14.1)/2)and(snre[i]<=14.1):mcs[19]+=1
        if(snre[i]>14.1)and(snre[i]<=14.1-(14.1-16.3)/2):mcs[20]+=1
        if(snre[i]>14.1-(14.1-16.3)/2)and(snre[i]<=16.3):mcs[21]+=1
        if(snre[i]>16.3)and(snre[i]<=16.3-(16.3-18.7)/2):mcs[22]+=1
        if(snre[i]>16.3-(16.3-18.7)/2)and(snre[i]<=18.7):mcs[23]+=1
        if(snre[i]>18.7)and(snre[i]<=18.7-(18.7-21)/2):mcs[24]+=1
        if(snre[i]>18.7-(18.7-21)/2)and(snre[i]<=21):mcs[25]+=1
        if(snre[i]>21)and(snre[i]<=21-(21-22.7)/2):mcs[26]+=1
        if(snre[i]>21-(21-22.7)/2)and(snre[i]<=22.7):mcs[27]+=1
        if(snre[i]>22.7):mcs[28]+=1
 
    return mcs

def db_to_linear(db):
    lin=10**(db/10)
    return lin
def linear_to_db(linear):
    db=10*np.log10(linear/10)
    return db
def linear_to_dbm(linear):
    dbm=10*np.log10(linear/10**-3)
    return dbm
def dbm_to_linear(dbm):
    linear=10**(-3)*10**(dbm/10)
    return linear
def CalcSINR(R,f):
    
    dPasso = R/10                        # Resolução do grid
    
    dDim = 5*R                          # Dimensão do grid
    ht = 32                             # Altura da antena transmissora em metros
    hr = 1.5                            # Altura da antena receptora em metros
    subR = R*np.sqrt(3)/2               # Curva ortogonal aos lados do Hexágono
    ptw = 20                            # Potência de transmissão em Watts
    ptdbm = linear_to_dbm(ptw)   # Potência de transmissão em dBm
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
    # Cálculo da potência recebida em cada ponto do grid recebida de cada ERB
    #Modelo Lhata hataurban cost231 para estimativa de perda de percurso
    ahre = 3.2*(np.log10(11.75*hr))**2 - 4.97 # Fator de correção para cidade grande
    Lhata1 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB1/1000)) + 3) 
    Lhata2 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB2/1000)) + 3) 
    Lhata3 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB3/1000)) + 3) 
    Lhata4 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB4/1000)) + 3) 
    Lhata5 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB5/1000)) + 3) 
    Lhata6 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB6/1000)) + 3) 
    Lhata7 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB7/1000)) + 3) 
    ruido=-106.98
    #conversão das potências em linear
    Lhata1lin=dbm_to_linear(Lhata1)
    Lhata2lin=dbm_to_linear(Lhata2)
    Lhata3lin=dbm_to_linear(Lhata3)
    Lhata4lin=dbm_to_linear(Lhata4)
    Lhata5lin=dbm_to_linear(Lhata5)
    Lhata6lin=dbm_to_linear(Lhata6)
    Lhata7lin=dbm_to_linear(Lhata7)
    ruidolin=dbm_to_linear(ruido)
    #calculo das interferencias
    interf1=Lhata2lin+Lhata3lin+Lhata4lin+Lhata5lin+Lhata6lin+Lhata7lin+ruidolin
    interf2=Lhata1lin+Lhata3lin+Lhata4lin+Lhata5lin+Lhata6lin+Lhata7lin+ruidolin
    interf3=Lhata2lin+Lhata1lin+Lhata4lin+Lhata5lin+Lhata6lin+Lhata7lin+ruidolin
    interf4=Lhata2lin+Lhata3lin+Lhata1lin+Lhata5lin+Lhata6lin+Lhata7lin+ruidolin
    interf5=Lhata2lin+Lhata3lin+Lhata4lin+Lhata1lin+Lhata6lin+Lhata7lin+ruidolin
    interf6=Lhata2lin+Lhata3lin+Lhata4lin+Lhata5lin+Lhata1lin+Lhata7lin+ruidolin
    interf7=Lhata2lin+Lhata3lin+Lhata4lin+Lhata5lin+Lhata6lin+Lhata1lin+ruidolin
    #Calculo das SINR
    SINR1=Lhata1lin/interf1
    SINR2=Lhata2lin/interf2
    SINR3=Lhata3lin/interf3
    SINR4=Lhata4lin/interf4
    SINR5=Lhata5lin/interf5
    SINR6=Lhata6lin/interf6
    SINR7=Lhata7lin/interf7
    #Caculo para as melhores SINR
    SINRaux1=np.maximum(SINR1,SINR2)
    SINRaux2=np.maximum(SINRaux1,SINR3)
    SINRaux3=np.maximum(SINRaux2,SINR4)
    SINRaux4=np.maximum(SINRaux3,SINR5)
    SINRaux5=np.maximum(SINRaux4,SINR6)
    SINR_Maxima=np.maximum(SINRaux5,SINR7)

    SINR_Maximadb=linear_to_db(SINR_Maxima)#Convertendo a SINR para dB
    vetorSINR=np.matrix.flatten(SINR_Maximadb)#Transformando a Matriz em um array
    return vetorSINR
labels=['50','100','500','1000']
count=0
x = np.arange(len(labels))
for raio in [50,100,500,1000]:
    SNR=CalcSINR(raio,1900)*0.9
    mcs=QMCS(SNR)
    count+=1
    for i in range(29):
        if(i<9):
            plt.figure(1)
            plt.subplot(3, 3,i+1)
        if ((i>=9) and (i<18)):
            plt.figure(2)
            plt.subplot(3, 3,i-8)
        if ((i>=18) and (i<=29)):
            plt.figure(3)
            plt.subplot(4,3,i-17)
        plt.bar(count,mcs[i],width=0.35,label=str(raio))
       
plt.figure(1)
plt.xlabel('MCS')
plt.ylabel("Numero de vezes")
#plt.grid()
plt.legend()       
plt.tight_layout()
plt.figure(2)
plt.xlabel('MCS')
plt.ylabel("Numero de vezes")
#plt.grid()
plt.legend()  
plt.tight_layout()
plt.figure(3)
plt.xlabel('MCS')
plt.ylabel("Numero de vezes")
#plt.grid()
plt.legend()  
plt.tight_layout()
plt.show()         
    