import os
import numpy as np
from astropy.io import ascii
from astropy.table import Table

os.mkdir('sample_lcs')

n_lightcurves = 10

for i in range(n_lightcurves):
    times = np.linspace(0, 10, 100)
    sigma = np.random.rand()
    fluxes = (10 + sigma * np.random.randn(len(times)) +
              np.polyval([(0.5 - np.random.rand()), np.random.rand()], (times - 10*np.random.rand())))
    uncertainties = sigma * np.ones_like(fluxes)
    flags = np.random.randint(0, 5, len(fluxes))

    data = [times, fluxes, uncertainties, flags] 
    np.savetxt('sample_lcs/lc_{0}.txt'.format(i), data)
