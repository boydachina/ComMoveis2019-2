import numpy as np
def calculateReceivePower(Ga, Xs, ptx, Lp):
# PURPOSE: C�lculo da pot�ncia recebida (pode ser um vetor) em Watts
#
# USAGE: vtPr = calculateReceivePower(Ga, Xs, ptx, Lp)
#
# INPUTS:
# - Ga: ganho da antena (pode ser um vetor) em dBi
# - Xs: amostra de shadowing (pode ser um vetor) em dB
# - ptx: pot�ncia de transmiss�o (pode ser um vetor) em W
# - Lp: Perda de Percurso (pode ser um vetor) em escala linear
#
# OUTPUTS:
#  - vtPr: vetor coluna com as pot�ncias recebidas em Watts
#
# EXAMPLE: vtPr1 = calculateReceivePower(16, [-1.1853 ; -0.7236 ], 0.1250, [5.2727;1.0278]*1e8)
#
# SEE ALSO: fUL_sim_Skelenton
#
##############################################################################
# AUTHOR(S): Vicente 
# LAST UPDATE: 2015-05-31 at 16:00h
# REFERENCES:
# COPYRIGHT 2015 by UFRN
##############################################################################
##############################################################################
# TRANSLATE TO PYTHON: Vítor Gabriel Lemos Lopes
# LAST UPDATE: 2019-11-21
##############################################################################     
    dbm= 10*np.log10(np.array(ptx)/1e-3)-10*np.log10(np.array(Lp)/10)+np.array(Ga)+np.ndarray.flatten(Xs)
    vtPr=(1e-3)*10**(dbm/10)
    return vtPr
#vtPr1 = calculateReceivePower(16, [[-1.1853], [-0.7236 ]], 0.1250, np.array([[5.2727],[1.0278]])*1e8)
#print(vtPr1)