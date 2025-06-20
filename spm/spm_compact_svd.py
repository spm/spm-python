from spm._runtime import Runtime


def spm_compact_svd(*args, **kwargs):
    """
      Local SVD with compact support for large matrices  
        FORMAT U = spm_compact_svd(Y,xyz,nu)  
        Y     - matrix  
        xyz   - location  
        nu    - number of vectors  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_compact_svd.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_compact_svd", *args, **kwargs)
