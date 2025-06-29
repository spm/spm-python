from spm._runtime import Runtime


def det2x2(*args, **kwargs):
    """
      DET2X2 computes determinant of matrix x, using explicit analytic definition  
        if size(x,1) < 4, otherwise use MATLAB det-function  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/src/det2x2.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("det2x2", *args, **kwargs)
