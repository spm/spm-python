from spm._runtime import Runtime


def spm_ness_N2Sp(*args, **kwargs):
    r"""
      Convert a Gaussian density into polynomial potential parameters    
        FORMAT Sp = spm_ness_N2Sp(m,C,[K])  
       --------------------------------------------------------------------------  
        m  - (Gaussian) mean  
        C  - (Gaussian) covariance  
        K  - Order of polynomial expansion (K = 3 corresponds to quadratic)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ness_N2Sp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ness_N2Sp", *args, **kwargs)
