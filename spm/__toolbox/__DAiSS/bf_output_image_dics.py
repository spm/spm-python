from mpython import Runtime


def bf_output_image_dics(*args, **kwargs):
    """
      Computes DICS image
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_dics.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_output_image_dics", *args, **kwargs)
