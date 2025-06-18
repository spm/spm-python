from mpython import Runtime


def bf_write_spmeeg(*args, **kwargs):
    """
      Writes out beamformer results as M/EEG dataset
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_write_spmeeg.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_write_spmeeg", *args, **kwargs)
