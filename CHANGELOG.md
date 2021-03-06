# ++++++++++++++++++++++++++++++++++
# Tracking changes to sharpener
# compared to v1.0
# ++++++++++++++++++++++++++++++++++

# README
- expanded the list of python packages necessary to run sharpener

# convert_unifts.py
- fct: coord_to_pix
    - added if-clauses to check for header values to avoid error messages

# cont_src.py
- fct: find_src_imsad
    - changed declaration of src_imsad_out
    - disabled if-clauses which check the header for additional axis and delete them (lines 402 - 426)
        - replaced this by wcs function dropaxis() 
    - replaced reading-in of the imsad output txt file with ascii.read
        - it seems that miriad can write files with different line lenghts (or for astropy different number of columns per line)
        - this a problem and I added a check function that handles the one case that I discovered
        - maybe another package like pybdsf would be better on the long run
    - added a function that generates a karma annotation file
    - replaced table making with astropy function
    - get pixels by using astropy skycoordinates instead of package function
    - replaced csv creation with astropy function
    - added option to plot image with detected sources overplotted
        - it uses astropy wcs
        - and the SkyCoords values of the sources
- fct: check_miriad_output
    - new function for update branch
    - checks that the number of columns in miriad imsad output is the same for all rows
    - so far, this is because of FFLAG
    - if no flag is found, then miriad does not create a column entry
    - this makes reading the file back in difficult
    - the function corrects this by adding a "-"

# spec_ex.py
    - changed src_id variable to reference the source ID from the CSV table instead of a new number
    - changed the if-clause which checks for nan-values in the list of ra/dec pixels to use the np.isnan function

# absorption_plot.py
- fct: abs_plot
    - added option to set source name as title in plot
    - added bbox_inches='tight' to saving of plot
    - added an option for multi-plot spectra
    - added an option for a fixed y-axis
- add fct: create_all_abs_plot()
    - works as a wrapper for abs_plot()
    - avoids having to do this in run_sharpener

# run_sharpener.py
- added new package PyPDF2 to merge pdfs created by the routine
- added new package zipfile (Python standard) to create zip files for all plots

# sdss_match
- new module to query SDSS
- match radio source catalogue and SDSS catalogue if enabled
- plots an overview image