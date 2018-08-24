import sys, string, os
import numpy as np
import yaml
import json
import glob

from astropy.io import fits, ascii
from astropy import units as u
from astropy.table import Table, Column, MaskedColumn

sys.path.append('/Users/maccagni/notebooks/sharpener/sharp_modules/')
import cont_src as cont_src
import convert_units as conv_units
import spec_ex as spec_ex
import abs_plot as abs_plot
from hi import *


__author__ = "Filippo Maccagni"
__copyright__ = "RadioLife"
__version__ = "1.0.0"
__email__ = "filippo.maccagni@gmail.com"
__status__ = "Development"



####################################################################################################

class sharpener:
	'''
	
	Class for spectral studies (find continuum sources, extract spectra, analyze spectra)
	
	'''

	C=2.99792458e5 #km/s
	HI=1.420405751e9 #Hz

	def __init__(self, file=None):
		'''
	
		Set logger for spectrum extraction
		Find config file
		If not specified by user load sharpener_default.yml
	
		'''

		file_default = '/Users/maccagni/notebooks/sharpener/sharpener_default.yml'

		if file != None:
			cfg = open(file)
		else:
			cfg = open(file_default)
		self.cfg_par = yaml.load(cfg)
	
		print(json.dumps(self.cfg_par, indent=4, sort_keys=True))

		self.set_dirs()

	def enable_task(self,config,task):

		a = config.get(task, False)
		print a
		if a:
			return a['enable']
		else:
			False

	def set_dirs(self):
		'''
	 
		Sets directory strucure and filenames
		Creates directory abs/ in basedir+beam and subdirectories spec/ and plot/

		OUTPUT:
			tab : table of catalog
			flux : flux of continuum sources abouve set threshold
	 
		'''

		key = 'general'

		self.workdir  = self.cfg_par[key].get('workdir', None)
		self.cubename = self.workdir + self.cfg_par[key].get('cubename', None)
		self.cfg_par[key]['cubename'] = self.cubename		
		self.contname = self.workdir + self.cfg_par[key].get('contname', None)
		self.cfg_par[key]['contname'] = self.contname	
		mircont = os.path.basename(self.contname)
		mircont = string.split(mircont,'.')[0]
		self.cfg_par[key]['mircontname']= mircont+'.mir'
		self.absdir  = self.workdir+'abs/'
		self.cfg_par[key]['absdir'] = self.absdir		
		self.specdir = self.workdir+'spec/'
		self.cfg_par[key]['specdir'] = self.specdir		
		self.plotdir = self.workdir+'plot/'
		self.cfg_par[key]['plotdir'] = self.plotdir	

		if os.path.exists(self.absdir) == False:
			 os.makedirs(self.absdir)           
		if os.path.exists(self.specdir) == False:
			 os.makedirs(self.specdir)
		if os.path.exists(self.plotdir) == False:
			 os.makedirs(self.plotdir)

	def go(self):
		'''
	 	Calls the following functions
		
		- cont_src
	 	 -- source_catalog
	 		finds sources above threshold in a catalog
	 	 -- mosaic_continuum
	 		creates mosaic of continuum images
	 	 -- find_src_imsad (continuum)
	 		finds sources in a continuum image using MIRIAD imsad source finder
		- spec_ex
		 -- abs_ex
			extracts spectra given 
		- abs_plot
		 -- abs_plot
			plots spectra
		'''
		catalog_table = str(self.cfg_par['general'].get('absdir')) + 'cat_src_sharpener.txt'

		# cont_sources
		task = 'source_catalog'

		if self.enable_task(self.cfg_par,task)==True:
			cont_src.source_catalog(self.cfg_par,catalog_table)
		
		task = 'mosaic_continuum'
		if self.enable_task(self.cfg_par,task) == True:
			cont_src.mosaic_continuum(self.cfg_par)


		task = 'source_finder'
		if self.enable_task(self.cfg_par,task) == True:
			cont_src.find_src_imsad(self.cfg_par)

		task = 'spec_ex'
		if self.enable_task(self.cfg_par,task) == True:
			spec_ex.abs_ex(self.cfg_par)

		task = 'abs_plot'
		if self.enable_task(self.cfg_par,task) == True:
			spectra = glob.glob(self.cfg_par['general']['specdir']+'/*.txt')
			for i in xrange(0,len(spectra)):
				spectra[i] = os.path.basename(spectra[i])
				abs_plot.abs_plot(spectra[i],self.cfg_par)



