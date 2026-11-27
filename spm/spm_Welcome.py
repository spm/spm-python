from spm._runtime import Runtime


def spm_Welcome(*args, **kwargs):
    r"""
      Open SPM's welcome splash screen  
        FORMAT F = spm_Welcome  
        F        - welcome figure handle  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_Welcome.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_Welcome", *args, **kwargs)
