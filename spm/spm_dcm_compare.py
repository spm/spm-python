from spm._runtime import Runtime


def spm_dcm_compare(*args, **kwargs):
    r"""
      Compare two or more estimated models  
        FORMAT spm_dcm_compare(P)  
         
        P  - a char or cell array of DCM filenames  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dcm_compare.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_compare", *args, **kwargs, nargout=0)
