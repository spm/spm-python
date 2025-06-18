from mpython import Runtime


def bf_output_image_kurtosis(*args, **kwargs):
    """
      Compute kurtosis image
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_kurtosis.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_output_image_kurtosis", *args, **kwargs)
