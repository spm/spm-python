from spm._runtime import Runtime


def spm_en(*args, **kwargs):
    r"""
      Euclidean normalization  
        FORMAT [X] = spm_en(X,[p])  
        X   - matrix  
        p   - optional polynomial detrend [default: []]  
       __________________________________________________________________________  
         
        spm_en performs a Euclidean normalization setting the column-wise sum of  
        squares to unity (leaving columns of zeros as zeros).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_en.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_en", *args, **kwargs)
