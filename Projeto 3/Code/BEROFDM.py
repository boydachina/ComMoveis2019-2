import matplotlib.pyplot as plt
import numpy as np
import math
import commpy
def Q_function(items):
    q = list(map(lambda x: math.erfc(x/(2)**(1/2))/2, items))
    return q
def PET(snr,M):
    #snr=EbN0dB+10*np.log10(np.log2(M))
    EbNo=10**(snr/10)
    k=np.log2(M)
    x=np.sqrt(3*k*EbNo/(M-1))
    ber=(4/k)*(1-1/np.sqrt(M))*np.asanyarray(Q_function(x))
    return ber
def PET_BPSK(snr):
    arg=np.sqrt(2*10**(snr/10))
    ber=Q_function(arg)
    return ber  
def BER_QAM(snr,M,b):
    #snr=EbN0dB+10*np.log10(np.log2(M))
    bit=np.random.randint(0,2,size=b)  #Criação da váriavel bit 1 ou 0
    qam=commpy.QAMModem(M)             #Fazendo mapeamento para a modula MQAM
    sinal=qam.modulate(bit)            #Fazendo a modulação
    jan=40                             #janela OFDM
    symbol=b/qam.num_bits_symbol       #quantidade de simbolos dada a modulação
    ite=int(symbol/jan)                #numero de iterações do loop dado pelo numero de simbolos dividido pela janela
    eb1=(sum(sinal*np.conj(sinal)))/len(sinal)            #Energia de bit
    sinalnorm=sinal/np.sqrt(eb1)                          # sinal normalizado
    #pet= []
    ber= []
    for s in range(len(snr)):
        bit_error=0
        sinalrecpt=[]
        for i in range(ite) :
            sinalrap=np.fft.ifft(sinalnorm[jan*i:jan*i+jan],jan)
            sinalrecpt.extend(sinalrap)
        eb=(sum(sinalrecpt*np.conj(sinalrecpt)))/len(sinalrecpt)/np.sqrt(eb1)           #Energia de bit
        noise=eb*10**(-snr/10)                              #variância do ruído
        AWGN= np.random.normal(0,np.sqrt(noise[s]/2),len(sinalrecpt)) - np.random.normal(0,np.sqrt(noise[s]/2),len(sinalrecpt))*1j
        sinaltime=sinalrecpt + AWGN                        #Somando o sinal de simbolos com o ruido AWGN
        sinalfreq=[]
        for j in range(ite):
            sinalfast=np.fft.fft(sinaltime[jan*j:jan*j+jan],jan)
            sinalfreq.extend(sinalfast*np.sqrt(eb1))
        #sinalcons.extend(sinalfreq)
        resultbit=qam.demodulate(sinalfreq,'hard')       #Receptor demodulando os simbolos recebidos
        bit_error=np.where(bit!=resultbit,1,0)            #Verificando quantos bits vieram errados
        ber.append((sum(bit_error))/b)
    return ber
def BER_PSK(EbN0dB,M,b):
    snr=EbN0dB+10*np.log10(np.log2(M))
    bit=np.random.randint(0,2,size=b)  #Criação da váriavel bit 1 ou 0
    psk=commpy.PSKModem(M)             #Fazendo mapeamento para a modula MQAM
    sinal=psk.modulate(bit)            #Fazendo a modulação
    jan=40                             #janela OFDM
    symbol=b/psk.num_bits_symbol       #quantidade de simbolos dada a modulação
    ite=int(symbol/jan)                #numero de iterações do loop dado pelo numero de simbolos dividido pela janela
    eb1=(sum(sinal*np.conj(sinal)))/len(sinal)            #Energia de bit
    sinalnorm=sinal/np.sqrt(eb1)                          # sinal normalizado
    ber= []
    for s in range(len(snr)):
        bit_error=0
        sinalrecpt=[]
        for i in range(ite) :
            sinalrap=np.fft.ifft(sinalnorm[jan*i:jan*i+jan],jan)
            sinalrecpt.extend(sinalrap)
        eb=(sum(sinalrecpt*np.conj(sinalrecpt)))/len(sinalrecpt)/np.sqrt(eb1)           #Energia de bit
        noise=eb*10**(-snr/10)                              #variância do ruído
        AWGN= np.random.normal(0,np.sqrt(noise[s]/2),len(sinalrecpt)) - np.random.normal(0,np.sqrt(noise[s]/2),len(sinalrecpt))*1j
        sinaltime=sinalrecpt + AWGN                        #Somando o sinal de simbolos com o ruido AWGN
        sinalfreq=[]
        for j in range(ite):
            sinalfast=np.fft.fft(sinaltime[jan*j:jan*j+jan],jan)
            sinalfreq.extend(sinalfast*np.sqrt(eb1))
        resultbit=psk.demodulate(sinalfreq,'hard')       #Receptor demodulando os simbolos recebidos
        bit_error=np.where(bit!=resultbit,1,0)            #Verificando quantos bits vieram errados
        ber.append((sum(bit_error))/b)
    return ber
M64qam=64
M256qam=256                             #Para 64qam 
MBPSK=2
b=120000
EbNo=np.arange(0,15,1)
pet64=PET(EbNo,M64qam)
ber64=BER_QAM(EbNo,M64qam,b)
pet256=PET(EbNo,M256qam)
ber256=BER_QAM(EbNo,M256qam,b)
petbpsk=PET_BPSK(EbNo)
berbpsk=BER_PSK(EbNo,MBPSK,b)
plt.semilogy(EbNo,ber64,"bs-.",label="Ber Simulada 64QAM")
plt.semilogy(EbNo,pet64,"yo--",label="Ber Teorica 64QAM")
plt.semilogy(EbNo,ber256,"rs-.",label="Ber Simulada 256QAM")
plt.semilogy(EbNo,pet256,"go--",label="Ber Teorica 256QAM")
plt.semilogy(EbNo,berbpsk,"ms-.",label="Ber Simulada BPSK")
plt.semilogy(EbNo,petbpsk,"co--",label="Ber Teorica BPSK")
plt.title("Gráfico da Taxa de Erro de Bit (BER) versus Eb/No para "+ str(b) +" bits")
plt.legend()
plt.grid()
plt.xlabel("Eb/N0")
plt.ylabel("Taxa de erro bit")
plt.yscale("log")
plt.show()

