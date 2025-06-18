from mpython import Runtime


def _reproducescript(*args, **kwargs):
    """
      This is a helper function to create a script that reproduces the analysis. It
        appends the configuration and the function call to a MATLAB script.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/reproducescript.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("reproducescript", *args, **kwargs, nargout=0)
