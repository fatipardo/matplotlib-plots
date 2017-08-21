import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

def combined_from_chi(rama, ramainit, peptidepath):
    """Plot ramachandran plot, combining the output of 'gmx chi' 
    input: xvg output of 'gmx chi' for a trajectory, xvg output of 'gmx chi' for the first frame, path for output
    output: ramachandran plot with initial values
    example:
    
    peptidepath='/Users/User/testplots/' #directory where output plots will be stored
    rmsfiles='rama_all.xvg' #output file from 'gmx chi'
    ramainitial='first_frame.xvg' #output file from 'gmx chi'
   
    combined_from_chi(rmsfiles,ramainitial, peptidepath) 
    
    """
    
    peptide=peptidepath+'_rama.svg' #output path and figure format
    
    ramafile=np.loadtxt(rama) #load gmx chi output for trajectory 
    x=ramafile[:,0]
    y=ramafile[:,1]
    
    firstframe=np.loadtxt(ramainit) #load gmx chi output for initial frame
    x1=firstframe[:,0]
    y1=firstframe[:,1]
    
    fig = plt.figure(figsize=(12, 10)) #define the size of the figure
    plt.subplot(111)
    # Next line define xrange, yrange. Notice that histogram2d will invert y, so we need to plot -y. 
    H1, xedges, yedges =np.histogram2d(-y,x, bins=90, range=[[-180, 180],[-180, 180]])
    plt.imshow(H1,extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], cmap=cm.binary, interpolation='none')
    cb = plt.colorbar()
    cb.set_label('Counts')
    #We are plotting the initial values on top of the histogram2d
    plt.subplot(111)
    #Defining the size of the points as 200
    plt.scatter(x1, y1, 200)
    plt.axis([-180, 180, -180, 180]) #xrange, yrange
    plt.rcParams.update({'font.size' : 25}) # changes font size of labels
    plt.rcParams.update({'axes.labelweight' : 'bold'}) #makes axes title bold
    plt.rcParams.update({'font.weight' : 'bold'}) # make tick labels bold 
    plt.xticks(rotation='vertical')
    plt.xlabel('Phi')
    plt.ylabel('Psi')
    plt.savefig(peptide)
    plt.show()
