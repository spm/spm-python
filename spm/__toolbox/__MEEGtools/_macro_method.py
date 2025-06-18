from mpython import Runtime


def _macro_method(*args, **kwargs):
    """
      MACRO_METHOD: Script to insert at the beginning of all the brainstorm class functions


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/private/macro_method.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("macro_method", *args, **kwargs)
