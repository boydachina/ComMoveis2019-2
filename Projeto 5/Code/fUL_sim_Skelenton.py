import numpy as np
import time
from calculateReceivePower import calculateReceivePower
from fDrawBs import fDrawBs
from fPosUsrSector import fPosUsrSector
from OkumuraHata import OkumuraHata
from shadowing import shadowing
from User2BSDistance import User2BSDistance
def fUL_sim_Skelenton( dUserPerSector, dR, nRep, resultFolder ):
# PURPOSE: Skeleton for modeling SINR on Uplink (simulation itself).
# Prot�tipo em software para modelagem da SINR do enlace reverso em
# um sistema WCDMA com uma camada de interfer�ncia co-canal e reuso 1 
#
# USAGE: fUL_sim( dUserPerSector, dR, nRep, resultFolder )
#
# INPUTS:
#  - dUserPerSector: Number of users per sector
#  - dR: Sector radius
#  - nRep: number of monte carlo repetitions
#  - resultFolder: folder to store simulation results
#
# OUTPUTS:
#  - Several files with simulation data
#
# EXAMPLE: fUL_sim( 10, 100, 10, 'sim_test' )
#
# SEE ALSO: fUL_sim
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
    tic = time.time()
    # General Channel model parameters
    ht = 30
    hr = 1.5
    fc = 1950
    Ga = 16
    SF = 128
    # envFlag: Ambiente:
    #    1. Urbano cidade grande
    #    2. Urbano cidade pequena/media
    envFlag = 1
    # Noise in dB
    pn_dB = -106.98 # dB
    # Noise in Linear
    pn = (1e-3)*10**( pn_dB / 10 ) # mW
    # Shadowing standard deviation
    sigma = 8 #dB
    # Transmitted power of interferers
    ptx_all_dBm = 21
    ptx_all = 10**(ptx_all_dBm/10)*1e-3
    # Transmitted power of central cell
    ptx_dBm = 21
    ptx = 10**(ptx_dBm/10)*1e-3
    # ERBs positioning
    vtBs = fDrawBs( dR )
    # Create the SINR vector to acummulate SINR values 
    vtSINR = [ ]
    #Create the Potência Recebida vector to acummulate received power values
    vtPotr=[]
    #Create the Potência transmitida vector to acummulate transmited power values
    vtPott=[]
    # Evaluate users only on central sector
    dCenter = vtBs[0]
    # Create the users position vector
    vtSectorPos = np.zeros( (dUserPerSector, 1) )
    #
    for isim in range(nRep):
        ## Environment creation
        # Matriz com a posi��o (complexa) de cada usu�rio de cada uma das 7
        # ERBS (a posi��o � relativa a sua ERB servidora)
        # Nas linhas: usu�rios
        # Nas colunas: ERB
        #print(str(isim))
        mtSectorPos=np.zeros((dUserPerSector,len(vtBs)),dtype=complex)
        for iS in range(len( vtBs )):
            dCenter = vtBs[ iS ]
            mtSectorPos[ :, iS ] = fPosUsrSector( dUserPerSector, dCenter, dR )
        
        # Dist�ncia dos usu�rios da c�lula central para a c�lula central (TODO: students implementation)
        dUserErbDistance = User2BSDistance( mtSectorPos, vtBs, 1 )
        # Pathloss (TODO: students implementation)
        Lp_dB = OkumuraHata( fc, ht, hr, dUserErbDistance/1e3, envFlag )
        Lp = 10**( Lp_dB/ 10 )
        # Shadowing (TODO: students implementation)
        Xs = shadowing( sigma, dUserPerSector )
        # Evaluation of the vector of receive powers of desired users to the
        # server BS (central cell) (TODO: students implementation)
        vtPr = calculateReceivePower(Ga, Xs, ptx, Lp)
        ## Interfer�ncia
        mtInter = []
        vtInterTotalPower = []
        for ibInter in range(1 , 7):
            # Central BS to Interferer users distance (TODO: students implementation)
            vtInter2BSDistance = User2BSDistance( mtSectorPos, vtBs, ibInter )
            # Pathloss (TODO: students implementation)
            Lp_dB_Inter = OkumuraHata( fc, ht, hr, vtInter2BSDistance/1e3, envFlag )
            Lp_Inter = 10**( Lp_dB_Inter / 10 )
            # Shadowing (TODO: students implementation)
            Xs_Inter = shadowing( sigma, dUserPerSector )
            # Interference power for user iusrInter
            vtInterPower = calculateReceivePower(Ga, Xs_Inter, ptx_all, Lp_Inter)
            # Interference power ( already combined per inteferer ERB )
            vtInterTotalPower.append(sum(vtInterPower))
            #vtInterTotalPower = [[ vtInterTotalPower],[sum( vtInterPower ) ]]
        
        vtInter = sum( vtInterTotalPower )
        ## Eb/No evaluation (herein called SINR)
        vtPr_dBm=10*np.log10((vtPr)/10**-3)
        vtPotr.extend(vtPr_dBm)
        vtPott.append(ptx_dBm)
        SINR = SF * vtPr / ( vtInter + pn )
        SINR_dB = 10*np.log10( SINR )
        vtSINR.extend(SINR_dB)


    #filename = ['UL_sim_users_' ,str(dUserPerSector), '_cellRadius_' ,str(dR) ,'_rep_' ,str(nRep) ,'.mat' ]
    #[SUCCESS,MESSAGE,MESSAGEID] = mkdir(resultFolder)
    #cd(resultFolder)
    toc = time.time()
    simTime=toc-tic
    #save( filename, 'vtSINR', 'simTime' )
    #cd('../')
    return vtSINR,vtPotr, vtPott
    #return simTime
#x,y,z=fUL_sim_Skelenton( 10, 100, 10, 'sim_test' )
#print(x)
#x1,y1,z1=fUL_sim_Skelenton( 10, 1000, 10, 'sim_test' )
#X=np.asarray(x1)-np.asarray(x)
#print(X)
