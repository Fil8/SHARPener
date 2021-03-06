sharpener_default
*****************

Configuration file for *SHARPener*. Content of sharpener_default.yml

:: 

    abs_plot:
        __helpstr: plot spectra from a given folder
        enable: true
        redshift_sources:
        - 800 2200
        title: true
        detailed_plot: true
        fixed_scale: false
    general:
        __helpstr: General INPUT directories and filenames
        contname: NGC315.Continuum.fits
        cubename: NGC315.Cube.fits
        verbose: false
        workdir: /home/<path>/beam00/
        plot_format: pdf
        merge_plots: true
    hanning:
        __helpstr: Hanning smoothing spectrum
        enable: false
        window: 3
        polynomial_subtraction:
        __helpstr: Subtract polynomial from spectrum to improve continuum subtraction
        degree_pol: 6
        enable: false
    sdss_match:
        __helpstr: Gets the SDSS sources for a give cube
        enable: true
        freq_min: 1130.0
        freq_max: 1430.0
        plot_image: true
        match_cat: true
        max_sep: 30
        min_radio_flux: 0
    simulate_continuum:
        __helpstr: Simulate continuum from source catalog output
        enable: false
    source_catalog:
        __helpstr: Find sources in a f.o.v. from source_catalog
        catalog: NVSS
        enable: false
        thresh: 30
        width: 5.2d
    source_finder:
        __helpstr: Find sources in continuum image using miriad imsad
        clip: 5e-3
        enable: true
        options: null
        region: null
        plot_image: true
    spec_ex:
        __helpstr: Extract spectra from datacube
        chrom_aberration: true
        enable: true
        flag_chans: null
        zunit: m/s
