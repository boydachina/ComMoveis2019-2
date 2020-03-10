import numpy as np
import matplotlib.pyplot as plt
def fDrawSector(dR,dCenter):
# PURPOSE: plot an hexagonal sector
#
# USAGE: fDrawSector(dR,dCenter)
#
# INPUTS:
#  - dCenter: Position of the Hexagonal center relative to central BS
#  - dR: Sector radius in Km
#
# OUTPUTS:
#  - plot of an hexagonal sector
#
# EXAMPLE: fDrawSector( 10, 0 )
#
##############################################################################
# AUTHOR(S): Yuri, Tarcisio, Waltemar, Vicente e Carlos
# LAST UPDATE: 2001-02-02 at 16:00h
# REFERENCES:
# COPYRIGHT 2001-2002 by Ericsson/UFC Cooperation
##############################################################################
# TRANSLATE TO PYTHON: Vítor Gabriel Lemos Lopes
# LAST UPDATE: 2019-11-15
##############################################################################  
    vtHex=[]
    for ie in range(1,7):
        vtHex.append(dR*(np.cos((ie-1)*np.pi/3)+1j*np.sin((ie-1)*np.pi/3)))
    vtHex=np.asarray(vtHex)+dCenter

    vtHexp=list(vtHex)
    vtHexp.append(vtHex[0])
    vtHexp=np.asarray(vtHexp)
    plt.plot(vtHexp.real,vtHexp.imag,'b')

