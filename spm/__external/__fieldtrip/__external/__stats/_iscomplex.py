from spm.__wrapper__ import Runtime


def _iscomplex(*args, **kwargs):
    """
    iscomplex is a function.  
          a = iscomplex(X)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/private/iscomplex.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("iscomplex", *args, **kwargs)
