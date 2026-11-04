from spm._runtime import Runtime


def spm_LAP_ph(*args, **kwargs):
    r"""
      Default precision function for LAP models (causal states)  
        FORMAT p = spm_LAP_ph(x,v,h,M)  
         
        x  - hidden states  
        v  - causal states  
        h  - precision parameters  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_LAP_ph.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_LAP_ph", *args, **kwargs)
