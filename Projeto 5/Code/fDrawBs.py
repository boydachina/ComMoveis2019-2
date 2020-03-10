import numpy as np
def fDrawBs( dR ):
# PURPOSE: Returns ERBs positions for a 7-cell one interference tier
# deployment
#
# USAGE: vtBs = fDrawBs( dR )
#
# INPUTS:
#  - dR: Sector radius 
#
# OUTPUTS:
#  - vtBs: Vector containing the ERBs positions 
#
# EXAMPLE: vtBs = fDrawBs( 100 );
#
# SEE ALSO: 
#
##############################################################################
# AUTHOR(S): Vicente 
# LAST UPDATE: 2015-05-31 at 16:00h
# REFERENCES:
# COPYRIGHT 2015 by UFRN
##############################################################################
##############################################################################
# TRANSLATE TO PYTHON: Vítor Gabriel Lemos Lopes
# LAST UPDATE: 2019-11-15
##############################################################################  
    vtBs =[0]
    offset = np.pi/6
    for iBs in range(1, 7):
        vtBs.append(dR*np.sqrt(3)*np.exp( 1j * ( (iBs-1)*np.pi/3 + offset ) ) )
    return vtBs


#vtBs = fDrawBs( 100 )
#print(vtBs)