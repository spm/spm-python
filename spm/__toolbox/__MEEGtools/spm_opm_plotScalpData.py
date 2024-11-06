from spm.__wrapper__ import Runtime


def spm_opm_plotScalpData(*args, **kwargs):
    """
      Display M/EEG interpolated sensor data on a scalp image  
        FORMAT D = spm_opm_amm(S)  
          S               - input structure  
         fields of S:  
          S.D             - SPM MEEG object                                - Default: no Default  
          S.T             - time point to initalise to                    - Default: first sample    
          S.display       - string to deermine what is plotted   -Default: 'RADIAL'  
        OUTPUT:  
          f          - the handle of the figure which displays the interpolated  
                       data  
       __________________________________________________________________________  
         
        This function creates a figure whose purpose is to display an  
        interpolation of the sensor data on the scalp (as an image).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_opm_plotScalpData.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_opm_plotScalpData", *args, **kwargs)
