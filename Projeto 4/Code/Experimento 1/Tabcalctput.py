import pandas as pd
from si_prefix import si_format
import numpy as np
tabela = pd.read_csv('TBSPRB.csv')#tabela de bits por tbs e numero de prbs
mcstbs= pd.read_csv('MCSTBS.csv')#tabela de mapeamento de MCS em TBS
def calcTput(mcs, freq, mimo, eqtab, prefic):
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
    if(eqtab=='tab'): #Calculo pela tabela
       
        tbs=mcstbs.loc[mcs,'TBS']
        bits=tabela.loc[tbs,str(prb)]
        Tput=bits*ca*mimo*cp/7*10**3
        return Tput
    if(eqtab=='eq'):#Calculo pela equação
        #Dado o valor de MCS a quantidade de bits por simbolo, e a taxa de codificação
        if(mcs==0):
            mod=2
            cod=0.1171875
        elif(mcs==1):
            mod=2
            cod=0.15332031
        elif(mcs==2):
            mod=2
            cod=0.18847656
        elif(mcs==3):
            mod=2
            cod=0.24511719
        elif(mcs==4):
            mod=2
            cod=0.3007125
        elif(mcs==5):
            mod=2
            cod=0.37011719
        elif(mcs==6):
            mod=2
            cod=0.43847656
        elif(mcs==7):
            mod=2
            cod=0.51367188
        elif(mcs==8):
            mod=2
            cod=0.58789063
        elif(mcs==9):
            mod=2
            cod=0.66308594
        elif(mcs==10):
            mod=4
            cod=0.33203125
        elif(mcs==11):
            mod=4
            cod=0.36914063
        elif(mcs==12):
            mod=4
            cod=0.42382813
        elif(mcs==13):
            mod=4
            cod=0.47851563
        elif(mcs==14):
            mod=4
            cod=0.54003906
        elif(mcs==15):
            mod=4
            cod=0.6015625
        elif(mcs==16):
            mod=4
            cod=0.64257813
        elif(mcs==17):
            mod=6
            cod=0.42773438
        elif(mcs==18):
            mod=6
            cod=0.45507813
        elif(mcs==19):
            mod=6
            cod=0.50488281
        elif(mcs==20):
            mod=6
            cod=0.55371094
        elif(mcs==21):
            mod=6
            cod=0.6015625
        elif(mcs==22):
            mod=6
            cod=0.65039063
        elif(mcs==23):
            mod=6
            cod=0.70214844
        elif(mcs==24):
            mod=6
            cod=0.75390625
        elif(mcs==25):
            mod=6
            cod=0.80273438
        elif(mcs==26):
            mod=6
            cod=0.85253906
        elif(mcs==27):
            mod=6
            cod=0.88867188
        elif(mcs==28):
            mod=6
            cod=0.92578125
        
        Tput=mimo*prb*cp*12*mod*0.75*ca*cod/(0.5*10**(-3))#25% de overhead,12 subportadoras
        return Tput
    else:
        print("Parâmetro errado")
#a=si_format(calcTput(28,20,'4x4','tab','normal'),precision=3)
#b=calcTput(28,20,'4x4','eq','normal')
#print(a+"bps")
MiMo=['1x1','2x2','4x4']
equacaotabela=['eq','tab']
frequencia=[1.4,3,5,10,15,20]
#dicionario com as colunas da tabela de Tput
finaltable={'MCS':['MCS','MCS'],
            'MIMO':['MIMO','MIMO'],
            'Taxa de Transmissão.1':['1.4MHZ','Equação'],
            'Taxa de Transmissão.2':['1.4MHZ','Tabela'],
            'Taxa de Transmissão.3':['3MHZ','Equação'],
            'Taxa de Transmissão.4':['3MHZ','Tabela'],
            'Taxa de Transmissão.5':['5MHZ','Equação'],
            'Taxa de Transmissão.6':['5MHZ','Tabela'],
            'Taxa de Transmissão.7':['10MHZ','Equação'],
            'Taxa de Transmissão.8':['10MHZ','Tabela'],
            'Taxa de Transmissão.9':['15MHZ','Equação'],
            'Taxa de Transmissão.10':['15MHZ','Tabela'],
            'Taxa de Transmissão.11':['20MHZ','Equação'],
            'Taxa de Transmissão.12':['20MHZ','Tabela']
            }
for mcs in range(29):
    for mimo in MiMo:
        cont=0
        finaltable['MIMO'].append(mimo)
        finaltable['MCS'].append(mcs)
        for freq in frequencia:
            for eqtab in equacaotabela:
                cont=cont+1
                finaltable['Taxa de Transmissão.'+str(cont)].append(si_format(calcTput(mcs,freq,mimo,eqtab,'normal'),precision=2)+'bps')
df = pd.DataFrame(finaltable, columns= ['MCS', 'MIMO','Taxa de Transmissão.1','Taxa de Transmissão.2','Taxa de Transmissão.3','Taxa de Transmissão.4','Taxa de Transmissão.5',
'Taxa de Transmissão.6','Taxa de Transmissão.7','Taxa de Transmissão.8','Taxa de Transmissão.9','Taxa de Transmissão.10','Taxa de Transmissão.11','Taxa de Transmissão.12'])
export_csv = df.to_csv('Release8.csv',index=None,header=True)#criando arquivo de tabela no local que está o código
#print(len(finaltable['MCS']))
#print(len(finaltable['MIMO']))
#print(len(finaltable['Taxa de Transmissão.1']))
MiMo=['1x1','2x2','4x4','8x8']
equacaotabela=['eq','tab']
frequencia=[1.4,3,5,10,15,20,100]
#dicionario com as colunas da tabela de Tput
finaltable2={'MCS':['MCS','MCS'],
            'MIMO':['MIMO','MIMO'],
            'Taxa de Transmissão.1':['1.4MHZ','Equação'],
            'Taxa de Transmissão.2':['1.4MHZ','Tabela'],
            'Taxa de Transmissão.3':['3MHZ','Equação'],
            'Taxa de Transmissão.4':['3MHZ','Tabela'],
            'Taxa de Transmissão.5':['5MHZ','Equação'],
            'Taxa de Transmissão.6':['5MHZ','Tabela'],
            'Taxa de Transmissão.7':['10MHZ','Equação'],
            'Taxa de Transmissão.8':['10MHZ','Tabela'],
            'Taxa de Transmissão.9':['15MHZ','Equação'],
            'Taxa de Transmissão.10':['15MHZ','Tabela'],
            'Taxa de Transmissão.11':['20MHZ','Equação'],
            'Taxa de Transmissão.12':['20MHZ','Tabela'],
            'Taxa de Transmissão.13':['100MHZ','Equação'],
            'Taxa de Transmissão.14':['100MHZ','Tabela']
            }
for mcs in range(29):
    for mimo in MiMo:
        cont=0
        finaltable2['MIMO'].append(mimo)
        finaltable2['MCS'].append(mcs)
        for freq in frequencia:
            for eqtab in equacaotabela:
                cont=cont+1
                finaltable2['Taxa de Transmissão.'+str(cont)].append(si_format(calcTput(mcs,freq,mimo,eqtab,'normal'),precision=2)+'bps')
df2 = pd.DataFrame(finaltable2, columns= ['MCS', 'MIMO','Taxa de Transmissão.1','Taxa de Transmissão.2','Taxa de Transmissão.3','Taxa de Transmissão.4','Taxa de Transmissão.5',
'Taxa de Transmissão.6','Taxa de Transmissão.7','Taxa de Transmissão.8','Taxa de Transmissão.9','Taxa de Transmissão.10','Taxa de Transmissão.11','Taxa de Transmissão.12','Taxa de Transmissão.13','Taxa de Transmissão.14'])
export_csv2 = df2.to_csv('Release10.csv',index=None,header=True)#criando arquivo de tabela no local que está o código

