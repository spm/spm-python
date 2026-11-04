from spm._runtime import Runtime


def spm_inline2func(*args, **kwargs):
    r"""
      Convert an inline object to a function handle  
        FORMAT [h] = spm_inline2func(f)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_inline2func.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_inline2func", *args, **kwargs)
