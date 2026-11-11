from spm._runtime import Runtime


def spm_hanning(*args, **kwargs):
    r"""
      Return the n-point Hanning window in a column vector  
        FORMAT H = spm_hanning(n)  
        n  -  length of hanning function  
        H  -  hanning function  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_hanning.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_hanning", *args, **kwargs)
