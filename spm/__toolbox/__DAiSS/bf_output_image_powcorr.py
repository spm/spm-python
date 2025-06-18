from mpython import Runtime


def bf_output_image_powcorr(*args, **kwargs):
    """
      Compute phase-amplitude coupling
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_powcorr.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_output_image_powcorr", *args, **kwargs)
