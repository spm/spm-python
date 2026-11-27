from spm._runtime import Runtime


def spm_ness_Sp2p(*args, **kwargs):
    r"""
      Convert a density into polynomial potential parameters    
        FORMAT p = spm_ness_Sp2p(Sp,x,[K])  
       --------------------------------------------------------------------------  
        Sp   - Polynomial coefficients or parameters of log density  
        x{i} - support (sample points): i = 1,...,N  
        K    - Order of polynomial expansion (K = 3 corresponds to quadratic)  
         
        p    - probability density  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ness_Sp2p.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ness_Sp2p", *args, **kwargs)
