import matplotlib.pyplot as plt
import numpy as np
import math
#snr=float(input("Digite o valor de Eb/N0 "))
b= int(input("Insira a quantidade de bits que vão ser transmitidos: "))
#O valor de eb/n0 
snr=np.arange(0,11,1)
snrlin=10**(snr/10)
eb=1                            #Energia de bits
noise=eb*10**(-snr/10)          #Variancia do ruido
pet= []
ber= []
for i in range(len(snr)):
    bit_error=0
    pet.append(0.5*math.erfc(np.sqrt(snrlin[i])))       #Probabilidade teorica
    AWGN= np.random.normal(0,np.sqrt(noise[i]/2),b)     #Ruido AWGN
    bit=np.random.randint(0,2,size=b)                   #Criação da váriavel bit 1 ou 0
    sinal=np.where(bit==0,-1,bit)                       #Transformação do bit 0 em -1
    sinalrecpt=sinal+AWGN                               #Somando o sinal de bits com o ruido AWGN
    resultbit=np.where(sinalrecpt>=0,1,-1)              #Receptor lendo os bits recebidos
    bit_error=np.where(sinal!=resultbit,1,0)            #Verificando quantos bits vieram errados
    ber.append((sum(bit_error))/b)                      #Probabilidade de erro na prática
#Plotando o gráfico
plt.semilogy(snr,ber,"bs-.",label="Ber Simulada")
plt.semilogy(snr,pet,"yo--",label="Ber Teorica")
plt.title("Gráfico da Taxa de Erro de Bit (BER) versus Eb/No para "+ str(b) +" bits")
plt.legend()
plt.grid()
plt.xlabel("Eb/N0")
plt.ylabel("Taxa de erro bit")
plt.yscale("log")
plt.show()
