import time
from fUL_sim_Skelenton import fUL_sim_Skelenton
import numpy as np
import matplotlib.pyplot as plt
# PURPOSE: Skeleton for modeling simulation campaign to evaluate SINR on
# Uplink. Prot�tipo em software para modelagem da SINR do enlace reverso em
# um sistema WCDMA com uma camada de interfer�ncia co-canal e reuso 1 
#
# USAGE: UL_simulations_campaign
#
# INPUTS:
#  - 
#
# OUTPUTS:
#  - Several files with simulation data
#
# EXAMPLE: UL_simulations_campaign
#
# SEE ALSO: fUL_sim
#
##############################################################################
# AUTHOR(S): Vicente 
# LAST UPDATE: 2015-05-31 at 16:00h
# REFERENCES:
# COPYRIGHT 2015 by UFRN
##############################################################################
# Dica: comente a linha a seguir para debugar (sen�o os breakpoints s�o deletados
# a cada execu��o do programa) 
##############################################################################
# TRANSLATE TO PYTHON: Vítor Gabriel Lemos Lopes
# LAST UPDATE: 2019-11-24
##############################################################################  
def cdf(data):

    data_size=len(data)

    # Set bins edges
    data_set=sorted(set(data))
    bins=np.append(data_set, data_set[-1]+1)

    # Use the histogram function to bin the data
    counts, bin_edges = np.histogram(data, bins=bins, density=False)

    counts=counts.astype(float)/data_size

    # Find the cdf
    cdf = np.cumsum(counts)

    return bin_edges[0:-1], cdf
Q=int(input('Gráfico para qual questão? Questão:'))
tic=time.time()
if(Q==2 or Q==3):
    vtdR = [ 50, 100, 500, 2000, 10000 ]# Cell radius to simulate [m]
    if(Q==2):
        vtUsersPerCell = [ 200 ]# System load (users per cell to simulate)
    if(Q==3):
        vtUsersPerCell = [ 10 ]# System load (users per cell to simulate)
if(Q==4):
    vtdR=[100]# Cell radius to simulate [m]
    vtUsersPerCell = [10,50, 200 ,1000]# System load (users per cell to simulate)
#
# Cell radius to simulate [m]

# Number of cell radius to simulate
ndR = len( vtdR )

# Number of System load points to simulate
nUsr = len( vtUsersPerCell )
# Monte Carlo Repetitions (it can be a vector)
vtRep = [1000]
# Number of  Monte Carlo Repetitions points to simulate
#nTotalRep = len( vtRep )
# Monte Carlo Repetitions Loop
for iRep in (vtRep) :
    resultFolder = ['sim_Rep_', str(iRep)]    
    # Cell radius Loop
    print(str(iRep))
    for idR in range (ndR):
        # Display simulation campaign status information
        print([str( 100 * (idR * nUsr )/ ( ndR * nUsr ) )+ ' # of all simulations have already done...'])
        # Current cell radius
        dR = vtdR[ idR ]
        # User per cell (load) loop
        for iusr in range (nUsr):
            # Current load
            dUserPerSector = vtUsersPerCell[ iusr ]
            # Display simulation information
            print(['Running simulation with cell Radius of '+ str(dR) +' and load of '+ str(dUserPerSector) +'...'])
            # Run simulation
            edgept=np.zeros(2)
            cdfpt=np.zeros(2)
            SINR,PR,PT=fUL_sim_Skelenton( dUserPerSector, dR, iRep, resultFolder )
            edgesinr,cdfsinr=cdf(SINR)
            edgepr,cdfpr=cdf(PR)
            edgept[1],cdfpt[1]=cdf(PT)
            edgept[0]=21
            plt.figure(1)
            plt.plot(edgesinr,cdfsinr,'-',label='CDF da SINR de Raio '+str(dR)+'m'+ " e "+str(dUserPerSector)+" usuários")
            plt.figure(2)
            plt.plot(edgepr,cdfpr,'-',label='CDF da Potência Recebida de Raio '+str(dR)+'m'+ " e "+str(dUserPerSector)+" usuários")
            if(Q!=3):
                plt.figure(3)
                plt.plot(edgept,cdfpt,'-o',label='CDF da potência Transmitida de Raio '+str(dR)+'m'+ " e "+str(dUserPerSector)+" usuários")
            #
# display simulation campaing duration
toc=time.time()
CampTime = toc-tic
print(['Simulation campaing duration = '+ str(CampTime)+ ' s'])
plt.figure(1)
plt.title("CDF da SINR")
#plt.ylim((0,1))
plt.ylabel("CDF")
plt.xlabel('SINR em dB')
plt.legend()
plt.grid()
plt.figure(2)
plt.title("CDF da Potência recebida")
#plt.ylim((0,1))
plt.ylabel("CDF")
plt.xlabel('Potência recebida em dBm')
plt.legend()
plt.grid()
if(Q!=3):
    plt.figure(3)
    plt.title("CDF da Potência Transmitida")
    #plt.ylim((0,1))
    plt.ylabel("CDF")
    plt.xlabel('Potência Transmitida em dBm')
    plt.legend()
    plt.grid()
plt.show()