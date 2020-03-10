#Aluno: Vítor Gabriel Lemos Lopes
#Projeto de Comunicações Móveis
import matplotlib.pyplot as plt
import numpy as np


R = float(input("Insira o valor do raio em metros:"))
f = float(input("Insira o valor da frequência em MHz:"))
dPasso = 50                         # Resolução do grid
dDim = 5*R                          # Dimensão do grid
ht = 32                             # Altura da antena transmissora em metros
hr = 1.5                            # Altura da antena receptora em metros
subR = R*np.sqrt(3)/2               # Curva ortogonal aos lados do Hexágono
ptw = 20                            # Potência de transmissão em Watts
ptdbm = 10*np.log10(ptw/(10**-3))   # Potência de transmissão em dBm

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
# Modelo Lhata hataurban cost231 para estimativa de perda de percurso
shadow= 8*np.random.randn(len(ERB1),len(ERB1[0])) #Para ficar todos do mesmo tamanho em quantidade de pontos foi escolhido uma ERB qualquer
ahre = 3.2*(np.log10(11.75*hr))**2 - 4.97 # Fator de correção para cidade grande
Lhata1 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB1/1000)) + 3)-shadow
Lhata2 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB2/1000)) + 3)-shadow
Lhata3 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB3/1000)) + 3)-shadow
Lhata4 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB4/1000)) + 3)-shadow
Lhata5 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB5/1000)) + 3)-shadow
Lhata6 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB6/1000)) + 3)-shadow
Lhata7 = ptdbm - (46.3 + 33.9*np.log10(f) - 13.82*np.log10(ht) - ahre + (44.9 - 6.55*np.log10(ht))*np.log10(np.absolute(ERB7/1000)) + 3)-shadow
#Cálculo da melhor potência
Aux1 = np.maximum(Lhata1,Lhata2)
Aux2 = np.maximum(Aux1,Lhata3)
Aux3 = np.maximum(Aux2,Lhata4)
Aux4 = np.maximum(Aux3,Lhata5)
Aux5 = np.maximum(Aux4,Lhata6)
Valor_Maximo = np.maximum(Aux5,Lhata7)

plt.pcolor(Valor_Maximo,cmap='jet') 
plt.grid()
plt.colorbar(label="Potência em DB")
plt.title(["Path Loss com sombreamento e raio de " + str(R) + "M"])
plt.xlabel("Distância em x10² M")
plt.ylabel("Distância em x10² M")
plt.show()