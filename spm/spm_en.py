from spm.__wrapper__ import Runtime


def spm_en(*args, **kwargs):
    """
      Euclidean normalization  
        FORMAT [X] = spm_en(X,[p])  
        X   - matrix  
        p   - optional polynomial detrend [default: []]  
       __________________________________________________________________________  
         
        spm_en performs a Euclidean normalization setting the column-wise sum of  
        squares to unity (leaving columns of zeros as zeros).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_en.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_en", *args, **kwargs)
