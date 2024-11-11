from spm.__wrapper__ import Runtime


def spm_robust_average(*args, **kwargs):
    """
      Apply robust averaging routine to X sets  
        FORMAT [Y,W] = spm_robust_averaget(X, dim, ks)  
        X      - data matrix to be averaged  
        dim    - the dimension along which the function will work  
        ks     - offset of the weighting function (default: 3)  
         
        W      - estimated weights  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_robust_average.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_robust_average", *args, **kwargs)
