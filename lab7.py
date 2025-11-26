import numpy as np
#import matplotlib.pyplot as plt

def centroid(px1, py1, px2, py2, px3, py3, m1, m2, m3):
    positions = np.array([[px1, px2, px3], [py1, py2, py3]])
    mass = np.array([m1, m2, m3])
    
    cx = np.sum(positions[0, :]*mass) / np.sum(mass)
    cy = np.sum(positions[1, :]*mass) / np.sum(mass)
    tot_mass = np.sum(mass)
        
    
    
    #plt.plot(positions[0, :], positions[1, :],"bo" )
    #plt.plot(cx, cy,"r+")
    
    return tot_mass, cx, cy


