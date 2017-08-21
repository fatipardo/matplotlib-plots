import numpy as np
import matplotlib.pyplot as plt

def plot1dhist(rmsfile, peptide):
    """ Plot 1D histogram from an xvg file obtained from 'gmx rms'
    input: xvg file from 'gmx rms' and system name.
    output: shows 1D histogram
    example:
    peptide='peptide'
    rmsfiles='/Users/User/results/'
    plot1dhist(rmsfiles,peptide)
    """
    
    nfile=rmsfile+'all_rms.xvg'
    ramafile=np.loadtxt(nfile)
    ramitas=ramafile[:,1]
    n, bins, patches = plt.hist(ramitas, 50,(0, 0.45), normed=1, facecolor='blue', alpha=0.75)

    DSP='/Users/User/histograms/'
    
    #Saves text file with histogram value for each bin
    histfile=DSP+'hist_'+peptide+'.txt'
    np.savetxt(histfile,n,fmt='%.2f')
    
    #Saves text file with bin values
    binsfile=DSP+'bins.txt'
    np.savetxt(binsfile,bins,fmt='%.2f')
    
    print peptide
    
    plt.xlabel('rms')
    plt.ylabel('(counts*bin width)/total')
    plt.title(rmsfile)
    plt.axis([0, 0.45, 0, 35])
    plt.grid(True)

    plt.show()
