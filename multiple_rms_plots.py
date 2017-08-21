import numpy as np
import matplotlib.pyplot as plt

def plotrms(rmsfile, peptidepath):
    """Plot multiple RMSD calculations, 
    input: multiple (10) rms.xvg output from 'gmx rms'
    output: plot with overlay 10 rms calculations
    example:
    peptidepath='/Users/User/testplots/' #directory where plot will be printed
    rmsfiles='/Users/User/Results/' #directory where the 10 xvg files created from 'gmx rms' are stored
    plotrms(rmsfiles, peptidepath)
    
    """
    
    PlotX=[]
    PlotY=[]
    
    peptide=peptidepath+'.png' # Path where plots will be saved and figure format
    
    for run in xrange(10):
        nfile=rmsfile+'rms_alpha_run%d.xvg' % run # path and name of the 10 rms_alpha_run#.xvg files created by 'gmx rms'
        print nfile
        ramafile=np.loadtxt(nfile)
        PlotX.append(ramafile[:,0])
        PlotY.append(ramafile[:,1])
    
    fig = plt.figure(figsize=(10, 9))
    plt.subplot(111)
    # Is there a better way to plot the 10 lines at the same time?
    # The X values are divided by 1000 to change ps to ns 
    plt.plot(PlotX[0]/1000, PlotY[0], PlotX[1]/1000, PlotY[1], PlotX[2]/1000, PlotY[2],PlotX[3]/1000, PlotY[3], PlotX[4]/1000, PlotY[4],
             PlotX[5]/1000, PlotY[5], PlotX[6]/1000, PlotY[6], PlotX[7]/1000, PlotY[7],PlotX[8]/1000, PlotY[8], PlotX[9]/1000, PlotY[9] )
    plt.xlabel('time (ns)')
    plt.ylabel('RMS (nm)')
    plt.rcParams.update({'font.size' : 25}) # changes font size of labels
    plt.rcParams.update({'axes.labelweight' : 'bold'}) # makes axes title bold
    plt.rcParams.update({'font.weight' : 'bold'}) # make tick labels bold 
    plt.yticks(np.arange(0,0.5, 0.1)) # yrange (0, 0.5) with 0.1 increment
    plt.axis([0, 100, 0, 0.4]) #total 100 ns xrange (0,100) and yrange (0, 0.4)
    plt.savefig(peptide)
    plt.show()
