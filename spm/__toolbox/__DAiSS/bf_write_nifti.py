from mpython import Runtime


def bf_write_nifti(*args, **kwargs):
    """
      Writes out nifti images of beamformer results
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_write_nifti.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_write_nifti", *args, **kwargs)
