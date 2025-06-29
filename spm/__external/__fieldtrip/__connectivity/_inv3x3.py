from spm._runtime import Runtime


def _inv3x3(*args, **kwargs):
    """
      INV3X3 computes inverse of matrix x, using explicit analytic definition  
        if size(x) = [3 3 K M]  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/inv3x3.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("inv3x3", *args, **kwargs)
