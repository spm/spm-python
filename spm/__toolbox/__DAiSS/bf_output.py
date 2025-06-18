from mpython import Runtime


def bf_output(*args, **kwargs):
    """
      Perform postprocessing based on beamforming projectors
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_output", *args, **kwargs)
