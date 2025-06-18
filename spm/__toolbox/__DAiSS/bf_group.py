from mpython import Runtime


def bf_group(*args, **kwargs):
    """
      A module for applying a processing step to a group of subjects
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_group.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_group", *args, **kwargs)
