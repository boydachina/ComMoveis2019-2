import matplotlib.pyplot as plt
import numpy as np
#PURPOSE: Script for plotting simulations results for UL SINR. Prot�tipo
# em software para modelagem da SINR do enlace reverso em um sistema WCDMA com uma camada de interfer�ncia co-canal e reuso 1  
#
# USAGE: UL_plotting
#
# INPUTS:
#  - 
#
# OUTPUTS:
#  - Several files with simulation plots
#
# EXAMPLE: UL_plotting
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
# LAST UPDATE: 2019-11-24
##############################################################################  
# Cell radius to simulate
vtdR = [ 50, 100 ,500,2000, 10000] # metros
# Number of cell radius to simulate
ndR = len( vtdR )
# System load (users per cell to simulate)
vtUsersPerCell = [ 10, 50, 200, 1000 ]
# Number of System load points to simulate
nUsr = len( vtUsersPerCell )
# Monte Carlo Repetitions (it can not be a vector)
nRep = 1000
# Mount results folder
resultFolder = ['sim_Rep_', str(nRep)]
# Define plot colors and markers
chvtColor = ['r-s','b-o','m-*','c->','g-h']
#
# CDF for different cell radius (each line is a different value of load,
# i.e., users per cell). A set of figures, one for each Cell Radius.
#
# Cell radius Loop
for idR in range (ndR):
    # Current cell radius 
    dR = vtdR[idR ]
    # Create empty vectors to store plot handles and legend
    vtHandles = []
    chLegend = []
    # Get handle of figure 1 
    f1 = 1    
    # Load loop
    for iusr in range(nUsr):
        # Current load
        dUserPerSector = vtUsersPerCell[ iusr ]
        # Display process status information
        print(['Processing simulation results with cell Radius of '+ str(dR) +' and load of '+ str(dUserPerSector)+ '...'])
        # Call for figure 1
        plt.figure(f1)
        # Load results from file saved by simulation script
        filename = [resultFolder, filesep, 'UL_sim_users_', str(dUserPerSector), '_cellRadius_', str(dR) ,'_rep_', str(nRep) ,'.mat' ]
        #load(filename)
        # Call CDF plot and store its handle
        handle = cdfplot(vtSINR)
        # Plot linhas together
        plt.hold(True)
        # Store lines handles for future configuration
        vtHandles = [vtHandles, handle]
        # Store legend information for each line
        chLegend = [ chLegend , {['User load of ' ,str( dUserPerSector )]} ]
    
    plt.figure( f1 )
    fCDFmarkers_ok( vtHandles, 20 )
    plt.legend( chLegend )
    plt.setp(gca,'linewidth',3, 'fontsize',20,'FontWeight', 'bold')
    plt.setp(gcf,'Name','Simulation Results - UFRN - 2011','NumberTitle','off','color', [1, 1 ,1])
    outputFile = [ 'SINR_CDF_UserLoad_UL_sim_cellRadius_' ,str(dR), '_rep_' ,str(nRep) ]
    plt.title(['CDF (Radius = ' +str(dR)+ ', Repetitions = '+ str(nRep)+ ')'] )
    plt.ylabel(' CDF of SINR')
    plt.xlabel('SINR [dB]')
    print([ 'Saving file:  ', outputFile ] )
    #cd( resultFolder );
    #saveas(gcf, outputFile , 'fig')
    #cd('../')
    #close all;
    print([str( 100 * (idR * nUsr )/ ( ndR * nUsr ) ), ' # of all simulations have already done...'])

#
# CDF for different system load (each line is a different value of cell
# radius). A set of figures, one for each sytrem load.
#
for iusr in range( nUsr):
    dUserPerSector = vtUsersPerCell[iusr]
    vtHandles = []
    chLegend = []
    f2 = 2
    for idR in range (ndR):
        dR = vtdR [idR]
        print(['Processing simulation results with load of ', str(dUserPerSector), ' and cell Radius of ', str(dR), '...'])
        filename = [resultFolder, filesep, 'UL_sim_users_', str(dUserPerSector), '_cellRadius_', str(dR), '_rep_', str(nRep) ,'.mat' ]
        #load(filename)
        #handle = cdfplot(vtSINR)
        plt.hold(True)
        #vtHandles = [vtHandles, handle]
        chLegend = [ chLegend , {['Cell Radius of ', str( dR )]} ]
    
    plt.figure( f2 )
    #fCDFmarkers_ok( vtHandles, 20 )
    plt.legend( chLegend )
    plt.setp(gca,'linewidth',3, 'fontsize',20,'FontWeight', 'bold')
    plt.setp(gcf,'Name','Simulation Results - UFRN - 2011','NumberTitle','off','color', [1, 1, 1])
    outputFile = [ 'SINR_CDF_CellRadius_UL_sim_load_', str(dUserPerSector), '_rep_',str(nRep) ]
    plt.title(['CDF (Load = ' +str(dUserPerSector) +', Repetiotions = ' +str(nRep)+ ')'] )
    plt.ylabel(' CDF of SINR')
    plt.xlabel('SINR [dB]')
    print([ 'Saving file:  '+ outputFile ] )
    #cd( resultFolder )
    #saveas(gcf, outputFile , 'fig')
    #cd('../')
    
    print([str( 100 * (ndR * iusr )/ ( ndR * nUsr ) )+ ' # of all simulations have already done...'])

#
# A set of figures showing the average, 10th and 90th percentiles for different cell radius (each line is a different value of load,
# i.e., users per cell). A set of figures, one for each Cell Radius.
#

# Plot of average of metrics
f3 = 3
# Plot of 10th percentile of metrics
f4 = 4
# Plot of 90th percentile of metrics
f5 = 5
chLegend = []
for idR in range( ndR):
    dR = vtdR[idR ]
    vtAverageSINR  = []
    vt10thSINR  = []
    vt90thSINR  = []
    for iusr in range( nUsr):
        dUserPerSector = vtUsersPerCell[ iusr ]
        print(['Processing simulation results with cell Radius of '+ str(dR) +' and load of ' +str(dUserPerSector) +'...'])
        #filename = [resultFolder, filesep, 'UL_sim_users_', str(dUserPerSector), '_cellRadius_', str(dR) ,'_rep_', str(nRep) ,'.mat' ]
        #load(filename)
        vtAverageSINR  = [ vtAverageSINR, np.mean( vtSINR ) ]
        vt10thSINR  = [ vt10thSINR, np.percentile(vtSINR,10,interpolation='midpoint') ]
        vt90thSINR  = [ vt90thSINR, np.percentile(vtSINR,90,interpolation='midpoint') ]
    
    chLegend = [ chLegend , {['Cell Radius of ', str( dR )]} ]
    #
    # Average SINR plot
    plt.figure( f3 )
    plt.plot( vtUsersPerCell, vtAverageSINR, chvtColor[idR,:] )
    plt.hold(True)
    plt.legend( chLegend )
    plt.setp(gca,'linewidth',3, 'fontsize',20,'FontWeight', 'bold')
    plt.setp(gcf,'Name','Simulation Results - UFRN - 2011','NumberTitle','off','color', [1, 1 ,1])
    plt.title(['Average SINR (Repetitions = ' +str(nRep) +')'] )
    plt.ylabel('Average SINR [dB]')
    plt.xlabel('Load (users per cell)')
    #
    # 10th SINR plot
    plt.figure( f4 )
    plt.plot( vtUsersPerCell, vt10thSINR, chvtColor[idR,:] )
    plt.hold(True)
    plt.legend( chLegend )
    plt.setp(gca,'linewidth',3, 'fontsize',20,'FontWeight', 'bold')
    plt.setp(gcf,'Name','Simulation Results - UFRN - 2011','NumberTitle','off','color', [1, 1, 1])
    plt.title(['10th percetile SINR (Repetitions = ' +str(nRep)+ ')'] )
    plt.ylabel('10th percetile SINR [dB]')
    plt.xlabel('Load (users per cell)')
    #
    # 90th SINR plot
    plt.figure( f5 )
    plt.plot( vtUsersPerCell, vt90thSINR, chvtColor[idR,:] )
    plt.hold(True)
    plt.legend( chLegend )
    plt.setp(gca,'linewidth',3, 'fontsize',20,'FontWeight', 'bold')
    plt.setp(gcf,'Name','Simulation Results - UFRN - 2011','NumberTitle','off','color', [1, 1, 1])
    plt.title(['90th percetile SINR (Repetitions = ' +str(nRep)+ ')'] )
    plt.ylabel('90th percetile SINR [dB]')
    plt.xlabel('Load (users per cell)')
    #
    print([str( 100 * (idR * nUsr )/ ( ndR * nUsr ) ) +' # of all simulations have already done...'])

# Saving plots
figure(f3)
outputFile = [ 'SINR_UsersLoadAverageSINR_UL_sim_rep_' ,str(nRep) ]
print([ 'Saving file:  '+ outputFile ] )
#cd( resultFolder )
#saveas(gcf, outputFile , 'fig')
#cd('../')
#
figure(f4)
outputFile = [ 'SINR_UsersLoad10thSINR_UL_sim_rep_', str(nRep) ]
print([ 'Saving file:  '+ outputFile ] )
#cd( resultFolder )
#saveas(gcf, outputFile , 'fig')
#cd('../')
#
figure(f5)
outputFile = [ 'SINR_UsersLoad90thSINR_UL_sim_rep_', str(nRep) ]
print([ 'Saving file:  ', outputFile ] )
#cd( resultFolder )
#saveas(gcf, outputFile , 'fig')
#cd('../')
#
#
# A set of figures showing the average, 10th and 90th percentiles for different system load (each line is a different value of cell
# radius). A set of figures, one for each sytrem load.
#
#close all;
f6 = 6
f7 = 7
f8 = 8
chLegend = []
for iusr in range(nUsr):
    dUserPerSector = vtUsersPerCell[ iusr ]
    vtAverageSINR  = []
    vt10thSINR  = []
    vt90thSINR  = []
    for idR in range(ndR):
        dR = vtdR[ idR ]  
        print(['Processing simulation results with cell Radius of '+ str(dR) +' and load of '+ str(dUserPerSector)+ '...'])
        filename = [resultFolder, filesep ,'UL_sim_users_' ,str(dUserPerSector) ,'_cellRadius_' ,str(dR) ,'_rep_', str(nRep) ,'.mat' ]
        #load(filename)
        vtAverageSINR  = [ vtAverageSINR, np.mean( vtSINR ) ]
        vt10thSINR  = [ vt10thSINR, np.percentile(vtSINR,10,interpolation='midpoint') ]
        vt90thSINR  = [ vt90thSINR, np.percentile(vtSINR,90,interpolation='midpoint') ]
        
    
    chLegend = [ chLegend , {['User Load of ' ,str( dUserPerSector )]} ]
    # Average SINR plot
    plt.figure( f6 )
    plt.plot( vtdR, vtAverageSINR, chvtColor[iusr,:] )
    plt.hold(True)
    legend( chLegend )
    plt.setp(gca,'linewidth',3, 'fontsize',20,'FontWeight', 'bold')
    ṕlt.setp(gcf,'Name','Simulation Results - UFRN - 2011','NumberTitle','off','color', [1, 1, 1])
    plt.title(['Average SINR (Repetitions = '+ str(nRep)+ ')'] )
    plt.ylabel('Average SINR [dB]')
    plt.xlabel('Cell Radius (meters)')
    # 10th SINR plot
    figure( f7 )
    plot( vtdR, vt10thSINR, chvtColor[iusr,:] )
    plt.hold(True)
    plt.legend( chLegend )
    plt.setp(gca,'linewidth',3, 'fontsize',20,'FontWeight', 'bold')
    plt.setp(gcf,'Name','Simulation Results - UFRN - 2011','NumberTitle','off','color', [1, 1, 1])
    plt.title(['10th percetile SINR (Repetitions = '+ str(nRep) +')'] )
    plt.ylabel('10th percetile SINR [dB]')
    plt.xlabel('Cell Radius (meters)')    
    # 90th SINR plot
    figure( f8 )
    plt.plot( vtdR, vt90thSINR, chvtColor[iusr,:] )
    plt.hold(True)
    plt.legend( chLegend )
    plt.setp(gca,'linewidth',3, 'fontsize',20,'FontWeight', 'bold')
    plt.setp(gcf,'Name','Simulation Results - UFRN - 2011','NumberTitle','off','color', [1, 1 ,1])
    plt.title(['90th percetile SINR (Repetitions = '+ str(nRep)+ ')'] )
    plt.ylabel('90th percetile SINR [dB]')
    plt.xlabel('Cell Radius (meters)')
    
    print([str( 100 * (idR * nUsr )/ ( ndR * nUsr ) )+ ' # of all simulations have already done...'])

# Saving plots
figure(f6)
outputFile = [ 'SINR_CellRadiusAverageSINR_UL_sim_rep_', str(nRep) ]
print([ 'Saving file:  ', outputFile ] )
#cd( resultFolder );
#saveas(gcf, outputFile , 'fig')
#cd('../')
#
figure(f7)
outputFile = [ 'SINR_CellRadius10thSINR_UL_sim_rep_', str(nRep) ]
print([ 'Saving file:  '+ outputFile ] )
#cd( resultFolder );
#saveas(gcf, outputFile , 'fig')
#cd('../')
#
figure(f8)
outputFile = [ 'SINR_CellRadius90thSINR_UL_sim_rep_', str(nRep) ]
print([ 'Saving file:  ',+ outputFile ] )
#cd( resultFolder );
#saveas(gcf, outputFile , 'fig')
#cd('../');
#close all;
print('All plots are saved and closed.')