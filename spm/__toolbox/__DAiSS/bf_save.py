from mpython import Runtime


def bf_save(*args, **kwargs):
    """
      Save BF data in a MAT file
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_save.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_save", *args, **kwargs, nargout=0)
