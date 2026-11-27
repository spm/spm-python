from spm._runtime import Runtime


def spm_create_vol(*args, **kwargs):
    r"""
      Create a NIfTI image volume  
        FORMAT V = spm_create_vol(V)  
        V        - image volume information (see spm_vol.m)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_create_vol.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_create_vol", *args, **kwargs)
