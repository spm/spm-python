from mpython import Runtime


def _varsize(*args, **kwargs):
    """
      VARSIZE returns the size of a variable in bytes. It can be used on any MATLAB
        variable, including structures and cell arrays.

        See also WHOS


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/varsize.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("varsize", *args, **kwargs)
