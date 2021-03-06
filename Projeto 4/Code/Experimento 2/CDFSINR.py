#Aluno: Vítor Gabriel Lemos Lopes
#Projeto de Comunicações Móveis
import pandas as pd
from si_prefix import si_format
import numpy as np
import matplotlib.pyplot as plt
import math
tabela = pd.read_csv('TBSPRB.csv')#tabela de bits por tbs e numero de prbs
mcstbs= pd.read_csv('MCSTBS.csv')#tabela de mapeamento de MCS em TBS
def Q_function(x):
    q =math.erfc(x/(2)**(1/2))/2
    return q
def BER_QAM(EbN0dB,M):
    sqM= M**(1/2)
    ah = 2*(1-(sqM**(-1)))/np.log2(sqM)
    b= 6*np.log2(sqM)/(M-1)
    arg = (b*10**(EbN0dB/10))**(1/2)
    ber = ah*Q_function(arg)
    
    return ber
def calcTput(snre, freq, mimo,prefic):
    if(snre<-6.7):return 0, 0
    if(snre<=-4.7)and(snre>=-6.7):mcs=0
    if(snre>-4.7)and(snre<=-2.3):mcs=1
    if(snre>-2.3)and(snre<=-2.3-(-2.3-0.2)/2):mcs=2      
    if(snre>-2.3-(-2.3-0.2)/2)and(snre<=0.2):mcs=3
    if(snre>0.2)and(snre<=0.2-(0.2-2.4)/2):mcs=4
    if(snre>0.2-(0.2-2.4)/2)and(snre<=2.4):mcs=5
    if(snre>2.4)and(snre<=2.4-(2.4-4.3)/2):mcs=6
    if(snre>2.4-(2.4-4.3)/2)and(snre<=4.3):mcs=7       
    if(snre>4.3)and(snre<=4.3-(4.3-5.9)/3):mcs=8
    if(snre>4.3-(4.3-5.9)/3)and(snre<=4.3-(4.3-5.9)*2/3):mcs=9
    if(snre>4.3-(4.3-5.9)*2/3)and(snre<=5.9):mcs=10    
    if(snre>5.9)and(snre<=5.9-(5.9-8.1)/2):mcs=11
    if(snre>5.9-(5.9-8.1)/2)and(snre<=8.1):mcs=12
    if(snre>8.1)and(snre<=8.1-(8.1-10.3)/2):mcs=13
    if(snre>8.1-(8.1-10.3)/2)and(snre<=10.3):mcs=14
    if(snre>10.3)and(snre<=10.3-(10.3-11.7)/3):mcs=15  
    if(snre>10.3-(10.3-11.7)/3)and(snre<=10.3-(10.3-11.7)*2/3):mcs=16 
    if(snre>10.3-(10.3-11.7)*2/3)and(snre<=11.7):mcs=17
    if(snre>11.7)and(snre<=11.7-(11.7-14.1)/2):mcs=18
    if(snre>11.7-(11.7-14.1)/2)and(snre<=14.1):mcs=19
    if(snre>14.1)and(snre<=14.1-(14.1-16.3)/2):mcs=20
    if(snre>14.1-(14.1-16.3)/2)and(snre<=16.3):mcs=21
    if(snre>16.3)and(snre<=16.3-(16.3-18.7)/2):mcs=22
    if(snre>16.3-(16.3-18.7)/2)and(snre<=18.7):mcs=23
    if(snre>18.7)and(snre<=18.7-(18.7-21)/2):mcs=24
    if(snre>18.7-(18.7-21)/2)and(snre<=21):mcs=25
    if(snre>21)and(snre<=21-(21-22.7)/2):mcs=26
    if(snre>21-(21-22.7)/2)and(snre<=22.7):mcs=27
    if(snre>22.7):mcs=28
         
    if(mimo == '4x4'):
        mimo = 4
    if(mimo == '2x2'):
        mimo = 2
    if(mimo == '1x1'):
        mimo = 1
    if(mimo == '8x8'):
        mimo = 8
    #Valores da Banda de frequência em relação ao numero de prbs
    if(freq == 1.4):
        prb = 6
    if(freq == 3):
        prb = 15
    if(freq == 5):
        prb = 25
    if(freq == 10):
        prb = 50
    if(freq == 15):
        prb = 75
    if(freq == 20):
        prb = 100
    ca=1
    if(freq==100):
        prb=100
        ca=5
    if(prefic=='normal'):
        cp=7
    if(prefic=='extendido'):
        cp=6
    if((mcs>=0)and(mcs<=9)):M=4
    if((mcs>=10)and(mcs<=16)):M=16
    if(mcs>=16):M=64
    ber=BER_QAM(snre,M)
    tbs=mcstbs.loc[mcs,'TBS']
    bits=tabela.loc[tbs,str(prb)]
    Tput=bits*ca*mimo*cp/7*10**3
    return Tput,ber

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
    
    # Resolução do grid
    dPasso=R/10
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
def cdf(data):

    data_size=len(data)

    # Set bins edges
    data_set=sorted(set(data))
    bins=np.append(data_set, data_set[-1]+1)

    # Use the histogram function to bin the data
    counts, bin_edges = np.histogram(data, bins=bins, density=False)

    counts=counts.astype(float)/data_size

    # Find the cdf
    cdf = np.cumsum(counts)

    return bin_edges[0:-1], cdf
for raio in [50,100,500,1000]:
    SINR=CalcSINR(raio,1900)
    edge,the_cdf=cdf(SINR)
    plt.figure(1)
    if (raio==50):
        plt.plot(edge,the_cdf,'-o',label='CDF da SINR de Raio '+str(raio)+'m')
    else:
        plt.plot(edge,the_cdf,'-',label='CDF da SINR de Raio '+str(raio)+'m')
    Tput=[]
    eff=[]
    for t in range (len(SINR)):
        taxa,erro=calcTput(SINR[t]*0.9,20,'4x4','normal')
        Tput.append(taxa/10**6)
        eff.append(1-erro)
    edgetran,cdftran=cdf(Tput)
    plt.figure(2)
    if (raio==50):
        plt.plot(edgetran,cdftran,'-o',label='CDF da taxa de transmissão de Raio '+str(raio)+'m')
    else:
        plt.plot(edgetran,cdftran,'-',label='CDF da taxa de transmissão de Raio '+str(raio)+'m')
    Tputeff=np.asarray(Tput)*np.asarray(eff)
    edgetput,cdftput=cdf(Tputeff)
    plt.figure(3)
    if (raio==50):
        plt.plot(edgetput,cdftput,'-o',label='CDF do Throughput de Raio '+str(raio)+'m')
        continue
    plt.plot(edgetput,cdftput,'-',label='CDF do Throughput de Raio '+str(raio)+'m')
plt.figure(1)
plt.title("CDF da SINR")
#plt.ylim((0,1))
plt.ylabel("CDF")
plt.xlabel('SINR em dB')
plt.legend()
plt.grid()
plt.figure(2)
plt.title("CDF da Taxa de Transmissão")
#plt.ylim((0,1))
plt.ylabel("CDF")
plt.xlabel('Taxa em Mbps')
plt.legend()
plt.grid()
plt.figure(3)
plt.title("CDF da Throughput")
#plt.ylim((0,1))
plt.ylabel("CDF")
plt.xlabel('Taxa em Mbps')
plt.legend()
plt.grid()
plt.show()