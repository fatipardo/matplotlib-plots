import numpy as np
import matplotlib.pyplot as plt

def calculate_percentage(rmsfile):
    """Calculates the percentage of conformations above a certain RMS threshold 
    input: RMS.xvg (output from gmx rms)
    output: prints percentage
    example:
    rmsfiles='/Users/User/Results/' #directory storing the 10 xvg files generated from 'gmx rms'
    calculate_percentage(rmsfiles)
    """
    
    PlotY=[]
    for run in xrange(10):
        nfile=rmsfile+'rms_alpha_run%d.xvg' % run #the 10 xvg files
        #print nfile
        ramafile=np.loadtxt(nfile)
        PlotY.append(ramafile[:,1])
    
    total_count=0
    far_counts=0
    
    for i in xrange(10):
        for j in xrange(len(PlotY[i])):
            total_count=total_count+1
            if PlotY[i][j] > 0.1: #The threshold is hard-coded - _ - 
                far_counts=far_counts+1
                  
    far_fraction=(float(far_counts)/float(total_count))*100
    print "%.2f" % far_fraction
            
