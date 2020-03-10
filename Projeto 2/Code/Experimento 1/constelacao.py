import matplotlib.pyplot as plt
import numpy as np
#O valor de eb/n0 
snr5=5
snr10=10

b=100                                          #Quantidade de bits  
eb=1                                           #Energia de bit

#Variancia do ruido
no5=eb*10**(-snr5/10)
no10=eb*10**(-snr10/10)

#Criação do sinal ruido AWGN, com média 0 e variância no/2

AWGN5 = np.random.normal(0,np.sqrt(no5/2),b)- np.random.normal(0,np.sqrt(no5/2),b)*1j
AWGN10 = np.random.normal(0,np.sqrt(no10/2),b)- np.random.normal(0,np.sqrt(no10/2),b)*1j

bit=np.random.randint(0,2,size=b)              #Criação da váriavel bit 1 ou 0
sinal=np.where(bit==0,-1,bit)                  #Transformação do bit 0 em -1

#somando o sinal de bits com o ruido AWGN
sinalrecpt5=sinal+AWGN5                          
sinalrecpt10=sinal+AWGN10

#separando a parte real e a imaginária
X5=sinalrecpt5.real
Y5=sinalrecpt5.imag
X10=sinalrecpt10.real
Y10=sinalrecpt10.imag
zeros=np.zeros(b)
#plot dos sinais
plt.plot(X5,Y5, 'ro',label="Eb/N0=5dB")
plt.plot(X10,Y10, 'go',label="Eb/N0=10dB")
plt.plot(sinal,zeros,'bo',label="Sinal original")
#plt.axis([-2.5,2.5,-2.5,2.5])
plt.grid()
plt.legend()
plt.show()