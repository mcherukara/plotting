
# coding: utf-8

# # Make nice figures

# In[1]:

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
get_ipython().magic(u'matplotlib inline')


# # Load data

# In[2]:

histx=np.loadtxt('simplex_x.txt', skiprows=1)
histz=np.loadtxt('simplex_z.txt', skiprows=1)
print histx.shape, histz.shape


# In[3]:

xpts=np.linspace(0,histx.shape[0],histx.shape[0]+1)
zpts=np.linspace(0,histz.shape[0],histz.shape[0]+1)


# In[58]:

plt.style.use('seaborn-white')
#matplotlib.rc('xtick', labelsize=20) 
#matplotlib.rc('ytick', labelsize=20)
matplotlib.rc('font',family='Times New Roman')
matplotlib.rcParams['font.size'] = 20
plt.plot(xpts[1:],histx[:,0], 'C3o-')
plt.xlabel('Iterations')
plt.ylabel('FWHM ($\mu$m)')
plt.tight_layout()
plt.grid()
plt.tick_params(which='both', width=2)
plt.tick_params(which='major', length=7)
plt.tick_params(which='minor', length=5)
plt.savefig('figs/x_iters.png', dpi=200)


# In[55]:

plt.plot(zpts[1:],histz[:,0], 'C0o-')
plt.xlabel('Iterations')
plt.ylabel('FWHM ($\mu$m)')
plt.tight_layout()
plt.savefig('figs/z_iters.png', dpi=200)


# In[41]:

x,y,z=histx[:,2],histx[:,3], histx[:,0]
plt.tricontourf(x,y,z, 10, cmap='viridis')
plt.xlabel('Motor 1 (arb.)')
plt.ylabel('Motor 2 (arb.)')
plt.colorbar()
plt.tight_layout()
plt.savefig('figs/x_map.png', dpi=200)


# In[42]:

x,y,z=histz[:,2],histz[:,3], histz[:,0]
plt.tricontourf(x,y,z, 10, cmap='viridis')
plt.xlabel('Motor 1 (arb.)')
plt.ylabel('Motor 2 (arb.)')
plt.colorbar()
plt.tight_layout()
plt.savefig('figs/z_map.png', dpi=200)


