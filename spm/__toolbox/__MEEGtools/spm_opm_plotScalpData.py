from spm._runtime import Runtime


def spm_opm_plotScalpData(*args, **kwargs):
    r"""
      Display M/EEG interpolated sensor data on a scalp image  
        FORMAT D = spm_opm_amm(S)  
          S               - input structure  
         fields of S:  
          S.D             - SPM MEEG object                                - Default: no Default  
          S.T             - time point to initialise to                    - Default: first sample    
          S.display       - string to deermine what is plotted   -Default: 'RADIAL'  
        OUTPUT:  
          f          - the handle of the figure which displays the interpolated  
                       data  
       __________________________________________________________________________  
         
        This function creates a figure whose purpose is to display an  
        interpolation of the sensor data on the scalp (as an image).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_opm_plotScalpData.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_opm_plotScalpData", *args, **kwargs)
