from spm._runtime import Runtime


def spm_ness_Sp2p(*args, **kwargs):
    """
      Convert a density into polynomial potential parameters    
        FORMAT p = spm_ness_Sp2p(Sp,x,[K])  
       --------------------------------------------------------------------------  
        Sp   - Polynomial coefficients or parameters of log density  
        x{i} - support (sample points): i = 1,...,N  
        K    - Order of polynomial expansion (K = 3 corresponds to quadratic)  
         
        p    - probability density  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ness_Sp2p.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ness_Sp2p", *args, **kwargs)
