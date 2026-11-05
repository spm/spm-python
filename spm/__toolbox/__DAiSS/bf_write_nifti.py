from spm._runtime import Runtime


def bf_write_nifti(*args, **kwargs):
    r"""
      Writes out nifti images of beamformer results  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_write_nifti.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_write_nifti", *args, **kwargs)
