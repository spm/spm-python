from mpython import Runtime


def bf_data(*args, **kwargs):
    """
      Prepare the data and initialise the beamforming pipeline
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_data.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_data", *args, **kwargs)
