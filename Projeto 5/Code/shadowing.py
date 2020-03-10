import numpy as np
def shadowing( sigma, nSamples ):
# PURPOSE: C�lculo de perda devido ao shadowing em dB
#
# USAGE: Xs = shadowing( sigma, nSamples )
#
# INPUTS:
#
#  - sigma: standard deviation of shadowing in dB
#  - nSamples: number of shadowing samples
#
# OUTPUTS:
#  - Xs: a vector ( nSamples x 1) of shadowing samples in dB (one for each user)
#
# EXAMPLE: Xs = shadowing( 8, 10 )
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
    Xs=sigma*np.random.randn(nSamples,1)
    return Xs
#Xs = shadowing( 8, 10 )
#print(Xs)