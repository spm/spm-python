from spm.__wrapper__ import Runtime


def det3x3(*args, **kwargs):
    """
      DET3X3 computes determinant of matrix x, using explicit analytic definition  
        if size(x) = [3 3 K M]  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/src/det3x3.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("det3x3", *args, **kwargs)
