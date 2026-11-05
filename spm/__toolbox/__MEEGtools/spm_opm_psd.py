from spm._runtime import Runtime


def spm_opm_psd(*args, **kwargs):
    r"""
      Compute PSD for OPM data (for checking noise floor)  
        FORMAT [po,freq,sel] = spm_opm_psd(S)  
          S               - input structure  
         fields of S:  
          S.D             - SPM MEEG object                       - Default: no Default  
          S.triallength   - window size (ms)                      - Default: 1000  
          S.bc            - boolean to dc correct                 - Default: 0  
          S.channels      - channel  to estimate PSD from         - Default: 'ALL'  
          S.plot          - boolean to plot or not                - Default: 0  
          S.units         - units of measurement                  - Default: 'fT'  
          S.constant      - constant line to draw as reference    - Default: 15  
          S.wind          - function handle for window            - Default: @hanning  
       	S.selectbad		- highlights and enables selection of   
                            bad channels			                - Default: 0  
         
         
        Output:  
          psd             - power spectral density  
          f               - frequencies psd is sampled at  
       	indices			- selected channel index  
       						To get labels use:  
       							plotted_lab = chanlabels(S.D,S.channels);  
       							sel_lab = plotted_lab(sel);  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_opm_psd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_opm_psd", *args, **kwargs)
