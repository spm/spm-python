from spm._runtime import Runtime


def spm_fnirs_wavg(*args, **kwargs):
    r"""
      Average data across trials   
        FORMAT wy = spm_fnirs_wavg(y,ons,dur)  
         
        y    - data (eg, optical density changes)   
        ons  - onset of average window (eg, onset of tasks)  
        dur  - window size   
         
        wy   - time series averaged across trials  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_fnirs/spm_fnirs_wavg.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fnirs_wavg", *args, **kwargs)
