from spm._runtime import Runtime


def spm_zeros(*args, **kwargs):
    r"""
      Fill a cell or structure array with zeros  
        FORMAT [X] = spm_zeros(X)  
        X  - numeric, cell or structure array[s]  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_zeros.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_zeros", *args, **kwargs)
