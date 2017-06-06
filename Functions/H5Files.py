#!/usr/bin/env python3

### Projections pixel deviation
### author: Gustavo J. Q. Vasconcelos e Gabriel Schubert R. Costa
### email: gustavo.vasconcelos@lnls.br , gabriel.costa@lnls.br

import numpy as np
import h5py
#from matplotlib import pyplot as plt
import sys

def getArray(tomo_path, dark_path, flat_path):
	f_tomo = h5py.File(tomo_path, "r")
	f_dark = h5py.File(dark_path, "r")
	f_flat = h5py.File(flat_path, "r")

	i=1
	
	dark = np.asarray(f_dark["darks"][0]).astype(np.double)
	flat = np.asarray(f_flat["flats"][0]).astype(np.double)
	data_prev = np.asarray(f_tomo["images"][i]).astype(np.double)
	
	

	numberofprojections=f_tomo["images"].shape[0]
	
	return (numberofprojections, data_prev)
	


		
if __name__ == "__main__":
	tomo_path = sys.argv[1]
	dark_path = sys.argv[2]
	flat_path = sys.argv[3]

	getArray(tomo_path,dark_path,flat_path)
