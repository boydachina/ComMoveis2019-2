import matplotlib.pyplot as plt
import numpy as np
import math

b= 100000
#O valor de eb/n0 
snr=np.arange(0,36,1)
snrlin=10**(snr/10)
eb=1                            #Energia de bits
noise=eb*10**(-snr/10)          #Variancia do ruido
pet= []
ber= []
ray=[]
berawgn=[]
sigma=1                           #Parametro de Rayleigh
for i in range(len(snr)):
    bit_error=0
    pet.append(0.5*math.erfc(np.sqrt(snrlin[i])))       #Probabilidade teorica
    #ray.append(1/(4*snrlin[i]))
    ray.append(0.5*(1-np.sqrt(snrlin[i]/(1+snrlin[i]))))  #Probabilidade de Rayleigh
    #ray.append(0.5*(1-np.sqrt((eb/noise[i])/(1+eb/noise[i]))))
    #u=np.random.uniform(0,1,size=b)                       #Gerando função uniforme
    #ht=sigma*np.sqrt(-2*np.log(u))
    #ht=np.random.rayleigh(2,size=b)                 #Distribuição de Rayleigh
    ht= np.sqrt(np.random.normal(0,1,b)**2+np.random.normal(0,1,b)**2)/np.sqrt(2)
    AWGN= np.random.normal(0,np.sqrt(noise[i]/2),b)   #Ruido AWGN
    bit=np.random.randint(0,2,size=b)              #Criação da váriavel bit 1 ou 0
    sinal=np.where(bit==0,-1,bit)                  #Transformação do bit 0 em -1
    sinalrecpt=sinal*ht+AWGN                       #multiplicando o ht de rayleigh e somando o sinal de bits com o ruido AWGN
    sinalreceptawgn=sinal+AWGN                     #Somando o ruido AWGN
    resultbit=np.where(sinalrecpt>=0,1,-1)         #Receptor lendo os bits recebidos
    resultbitawgn=np.where(sinalreceptawgn>=0,1,-1)
    bit_error=np.where(sinal!=resultbit,1,0)      #verificando quantos bits vieram errados
    bit_errorawgn=np.where(sinal!=resultbitawgn,1,0)
    ber.append((sum(bit_error))/b)                      #probabilidade de erro na prática
    berawgn.append((sum(bit_errorawgn))/b)
#plotando o gráfico
plt.semilogy(snr,ber,"bs-.",label="Ber Simulada Rayleigh")
plt.semilogy(snr,ray,"yo--",label="Ber Teorica Raileigh")
plt.semilogy(snr,pet,"m^-",label="Ber Teorica AWGN")
plt.semilogy(snr,berawgn,"c*:",label="Ber Simulada AWGN")
plt.title("Gráfico da Taxa de Erro de Bit (BER) versus Eb/No para "+ str(b) +" bits")
plt.legend()
plt.grid()
plt.xlabel("Eb/N0")
plt.ylabel("Taxa de erro bit")
plt.axis([-1,36,10**-10,0.5])
#plt.yscale("log")
plt.show()
