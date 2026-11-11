from spm._runtime import Runtime


def spm_squeeze(*args, **kwargs):
    r"""
      Version of squeeze with the possibility to select the dimensions to remove  
        FORMAT  B = spm_squeeze(A, dim)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_squeeze.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_squeeze", *args, **kwargs)
