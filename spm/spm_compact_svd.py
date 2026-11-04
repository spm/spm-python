from spm._runtime import Runtime


def spm_compact_svd(*args, **kwargs):
    r"""
      Local SVD with compact support for large matrices  
        FORMAT U = spm_compact_svd(Y,xyz,nu)  
        Y     - matrix  
        xyz   - location  
        nu    - number of vectors  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_compact_svd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_compact_svd", *args, **kwargs)
