import numpy as np
def fPosUsrSector(dUsrPerSector, dCenter, dR ):
# PURPOSE: Returns users positions inside hexagonal sector
#
# USAGE: [vtSectorPos] = fPosUsrSector(dUserPerSector, dCenter, dR)
#
# INPUTS:
#  - dUserPerSector: Number of users per sector
#  - dCenter: Position of the Hexagonal center relative to central BS
#  - dR: Sector radius in Km
#
# OUTPUTS:
#  - vtPosSector: Vector containing the users positions 
#
# EXAMPLE: [vtPosSector] = fPosUsrSector(100, np.cos(np.pi/3)+1j*np.sin(np.pi/3), 1)
#
# SEE ALSO: fDrawUsr and fPosUsrBS

##############################################################################
# AUTHOR(S): Yuri, Tarcisio, Waltemar, Vicente e Carlos
# LAST UPDATE: 2001-02-02 at 16:00h
# REFERENCES:
# COPYRIGHT 2001-2002 by Ericsson/UFC Cooperation
##############################################################################
# TRANSLATE TO PYTHON: Vítor Gabriel Lemos Lopes
# LAST UPDATE: 2019-11-15
##############################################################################  
    vtPosSector=np.zeros((1,1))
    if(dUsrPerSector>0):
        #p1=(np.random.rand(1, 2*dUsrPerSector)-0.5)*2*dR
        #p2=(1j*(np.random.rand(1,2*dUsrPerSector)-0.5))*2*dR
        p = (np.random.rand(1, 2*dUsrPerSector)-0.5 + 1j*(np.random.rand(1,2*dUsrPerSector)-0.5))*(2*dR)
        #p = (nprandomrand(1, 2*dUsrPerSector) + j*(nprandomrand(1,2*dUsrPerSector)))*(dR)
        p=np.ndarray.flatten(p)
        vtPosSector = p
        
        ang = np.angle(p)*180/np.pi
        
        sector = np.floor(((ang < 0) * 360 + ang)/60)
        sector = np.array([sector,sector,sector+1,sector+1])
        sector = sector* np.pi/3
        sector = np.transpose(sector)
        sector[:,0] = dR*np.cos(sector[:,0]) - p.real
        sector[:,2] = dR*np.cos(sector[:,2]) - p.real
        
        sector[:,1] = dR*np.sin(sector[:,1]) - p.imag
        sector[:,3] = dR*np.sin(sector[:,3]) - p.imag
        a=np.array([sector[:,0].flatten(),sector[:,1].flatten(), np.zeros([len(p),1]).flatten()])
        b=np.array([sector[:,2].flatten(),sector[:,3].flatten(), np.zeros([len(p),1]).flatten()])
        #cr = np.cross([sector[:,1:2],np.zeros([len(p),1])], [sector[:,3:4], np.zeros([len(p),1])])
        a=np.transpose(a)
        b=np.transpose(b)
        cr = np.cross(a,b)
        cr = np.nonzero(np.ravel(cr[:,2])>0)
        
        vtPosSector = vtPosSector[cr] + dCenter
        
        if (len(vtPosSector)<= dUsrPerSector):
            vtPosSector = fPosUsrSector(dUsrPerSector, dCenter, dR )
            return vtPosSector
        else:
            vtPosSector = vtPosSector[1:dUsrPerSector+1]
            return vtPosSector

#x=fPosUsrSector(100, np.cos(np.pi/3)+1j*np.sin(np.pi/3), 1)
#print(x)