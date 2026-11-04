from spm._runtime import Runtime


def spm_MB_col(*args, **kwargs):
    r"""
      Return colours and marker size for number of partitions  
        FORMAT [col,bol,msz] = spm_MB_col(n)  
        n  - number of partitions  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_MB_col.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MB_col", *args, **kwargs)
