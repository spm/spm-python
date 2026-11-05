from spm._runtime import Runtime


def bf_write_spmeeg(*args, **kwargs):
    r"""
      Writes out beamformer results as M/EEG dataset  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_write_spmeeg.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_write_spmeeg", *args, **kwargs)
