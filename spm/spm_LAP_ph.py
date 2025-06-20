from spm._runtime import Runtime


def spm_LAP_ph(*args, **kwargs):
    """
      Default precision function for LAP models (causal states)  
        FORMAT p = spm_LAP_ph(x,v,h,M)  
         
        x  - hidden states  
        v  - causal states  
        h  - precision parameters  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_LAP_ph.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_LAP_ph", *args, **kwargs)
