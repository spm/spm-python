from spm.__wrapper__ import Runtime


def _ctranspose3x3(*args, **kwargs):
    """
      compute ctranspose of multiple 3x3 matrices, input is 3x3xN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/ctranspose3x3.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ctranspose3x3", *args, **kwargs)
