import numpy as np
def User2BSDistance(mtSectorPos, vtBs, iERBTarget):
# PURPOSE: Calcular a dist�ncia entre os usu�rios da ERB target
# identificada por "iERBTarget" e a ERB Central 
#
# USAGE: vtUser2BSDistance = User2BSDistance( mtSectorPos, vtBs, ibInter)
#
# INPUTS:
# - mtSectorPos: matriz com a posi��o (complexa) de cada usu�rio em rela��o
#                as 7 ERBS (linhas: usu�rios; e nas colunas: ERB)
# - vtBs: vetor com a posi��o de cada ERBs (a primeira posi��o � da ERB
#         Central e as demais s�o interferentes) 
# - iERBTarget: �ndice da ERB alvo para o c�lculo da dist�ncia
#
# OUTPUTS:
#  - vtUser2BSDistance: vetor coluna com as dist�ncias dos usu�rios da ERB
#                        identificada por "iERBTarget" e a ERB Central
#                        (dist�ncia na mesma unidade que mtSectorPos e vtBs) 
#
# EXAMPLE: para um grid com 2 ERBs:
#          vtUser2BSDistance = User2BSDistance(1e2*[0.11+0.34i 1.13+0.39i; -0.15+0.085i 0.52+0.27i], [0 75+43.3i], 1 ) 
#          vtUser2BSDistance = User2BSDistance(1e2*[0.11+0.34i 1.13+0.39i; -0.15+0.085i 0.52+0.27i], [0 75+43.3i], 2 ) 
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
# LAST UPDATE: 2019-11-20
##############################################################################  
    vtUser2BSDistance=np.absolute(mtSectorPos[:,iERBTarget])
    return vtUser2BSDistance
#a=np.array([[0.11+0.34j, 1.13+0.39j], [-0.15+0.085j, 0.52+0.27j]])
#x=User2BSDistance(a*1e2, [0, 75+43.3j], 1) 
#print(x)