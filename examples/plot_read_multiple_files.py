"""
============================================
Read multiple files using regular expression
============================================

This example shows how to read several SPC files which are located inside a
folder.

"""
from __future__ import print_function

import os

import matplotlib.pyplot as plt

from specio import specread

# Get the path to the data relatively to this example
DATA_PATH = os.path.dirname(__file__)

spc_filenames = os.path.join(DATA_PATH, 'data', '*.spc')
print('The SPC files will be search in: {}'.format(spc_filenames))

# Read the data
spectra = specread(spc_filenames)

# Plot the first spectra
plt.plot(spectra.wavelength,
         spectra.spectrum.T)

# We get the axis information by using the meta data of the first file read.
plt.xlabel(spectra.meta[0]['xlabel'])
plt.ylabel(spectra.meta[0]['ylabel'])
plt.show()