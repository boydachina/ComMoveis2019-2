import numpy as np
def OkumuraHata(fc, ht, hr, d, flag ):
# PURPOSE: C�lculo de perda de percurso com modelo OKUMURA HATA em dB
#
# USAGE: PL = OkumuraHata(fc, ht, hr, d, flag )
#
# INPUTS:
#
#  - fc: frequencia em MHz
#  - ht: altura da antena transmissora  (Tx) em metros
#  - hr: altura da antena receptora (Rx) em metros
#  - d: dist�ncia entre Tx e Rx em kilometros
#  - flag: Ambiente:
#    1. Urbano cidade grande
#    2. Urbano cidade pequena/media
#
# OUTPUTS:
#  - PL: perda em dB
#
# EXAMPLE: OkumuraHata(1950, 30, 1.5, 1, 1 )
#
# SEE ALSO: fUL_sim_Skelenton
#
##############################################################################
# AUTHOR(S): Vicente 
# LAST UPDATE: 2015-05-31 at 16:00h
# REFERENCES:
# COPYRIGHT 2015 by UFRN
##############################################################################
# TRANSLATE TO PYTHON: Vítor Gabriel Lemos Lopes
# LAST UPDATE: 2019-11-21
##############################################################################      
    PL=129.4 + 35.2 * np.log10(d)
    return PL
#x=OkumuraHata(1950, 30, 1.5, 1, 1 )
#x=10**(x/10)
#print(x)