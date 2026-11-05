from spm._runtime import Runtime


def spm_robust_average(*args, **kwargs):
    r"""
      Apply robust averaging routine to X sets  
        FORMAT [Y,W] = spm_robust_averaget(X, dim, ks)  
        X      - data matrix to be averaged  
        dim    - the dimension along which the function will work  
        ks     - offset of the weighting function (default: 3)  
         
        W      - estimated weights  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_robust_average.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_robust_average", *args, **kwargs)
