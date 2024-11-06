from spm.__wrapper__ import Runtime


def sandwich2x2(*args, **kwargs):
    """
      SANDWICH2X2 compute x*y*x' provided y is Hermitian and dimensionality is 2x2xN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/src/sandwich2x2.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("sandwich2x2", *args, **kwargs)
