from spm._runtime import Runtime


def spm_rand_mar(*args, **kwargs):
    r"""
      Generate random variates from an autoregressive process  
        FORMAT [y] = spm_rand_mar(m,n,a)  
        m   - time bins  
        n   - variates  
        a   - autoregression coefficients  
         
        see also: spm_rand_power_law  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_rand_mar.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_rand_mar", *args, **kwargs)
