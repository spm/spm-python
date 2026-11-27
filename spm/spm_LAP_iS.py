from spm._runtime import Runtime


def spm_LAP_iS(*args, **kwargs):
    r"""
      Default precision function for LAP models (hidden states)  
        FORMAT [iS] = spm_LAP_iS(p,R)  
         
        p{1} - vector of precisions for causal states (v)  
        p{2} - vector of precisions for hidden states (v)  
        R    - generalised precision matrix  
         
        iS   - precision matrix for generalised states (causal and then hidden)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_LAP_iS.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_LAP_iS", *args, **kwargs)
