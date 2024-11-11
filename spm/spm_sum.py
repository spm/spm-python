from spm.__wrapper__ import Runtime


def spm_sum(*args, **kwargs):
    """
      Sum of elements  
        FORMAT S = spm_sum(X,vecdim)  
         
        Compatibility layer for SUM for MATLAB < R2018b  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_sum.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sum", *args, **kwargs)
