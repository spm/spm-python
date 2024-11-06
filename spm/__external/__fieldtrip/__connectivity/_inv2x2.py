from spm.__wrapper__ import Runtime


def _inv2x2(*args, **kwargs):
    """
      INV2X2 computes inverse of matrix x, using explicit analytic definition  
        if size(x,1) < 4, otherwise use MATLAB inv-function  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/inv2x2.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("inv2x2", *args, **kwargs)
