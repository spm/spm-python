from spm.__wrapper__ import Runtime


def spm_ness_N2Sp(*args, **kwargs):
    """
      Convert a Gaussian density into polynomial potential parameters    
        FORMAT Sp = spm_ness_N2Sp(m,C,[K])  
       --------------------------------------------------------------------------  
        m  - (Gaussian) mean  
        C  - (Gaussian) covariance  
        K  - Order of polynomial expansion (K = 3 corresponds to quadratic)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ness_N2Sp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ness_N2Sp", *args, **kwargs)
