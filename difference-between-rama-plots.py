import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

cpname='test'
rama='/Users/User/peptide1/rama_all.xvg' 
rama2='/Users/User/peptide2/rama_all.xvg' 

ramafile=np.loadtxt(rama)
ramafile2=np.loadtxt(rama2)

x=ramafile[:,0]
y=ramafile[:,1]

x2=ramafile2[:,0]
y2=ramafile2[:,1]


figure = plt.figure(figsize=(16,4))

#First Plot
plt.subplot(131)
#Notice that I had to apply the symmetry operation to y and x in order to plot the mirror image
#This is particular to the case I had in mind when writing this script
#You may want to revise how you plot (-y, x) or (y, -x) 
H1, xedges, yedges =np.histogram2d(y,-x, bins=30, range=[[-180, 180],[-180, 180]])#(xedges, yedges))
plt.imshow(H1,extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], cmap=cm.binary)
cb = plt.colorbar()
cb.set_label('counts')
plt.title('%s symmetrized'% cpname) 
#print H1

#Second plot
plt.subplot(132)
H2, xedges2, yedges2 =np.histogram2d(-y2,x2, bins=30, range=[[-180, 180],[-180, 180]])#(xedges, yedges))
plt.imshow(H2, extent=[xedges2[0], xedges2[-1], yedges2[0], yedges2[-1]], cmap=cm.binary)
cb = plt.colorbar()
cb.set_label('counts')
plt.title('%s 0001'% cpname) 

#Third plot 
plt.subplot(133)
h3a = H1-H2
mx=sorted([max(h3a.flatten()),-min(h3a.flatten())], reverse=True)[0]
plt.imshow(H1-H2,extent=[xedges2[0], xedges2[-1], yedges2[0], yedges2[-1]], cmap=cm.bwr, vmin=-mx, vmax=mx)
cb = plt.colorbar()
cb.set_label('counts')
plt.title('%s difference'% cpname) 


#Notice that this script will only show the plots, but will not save them.
