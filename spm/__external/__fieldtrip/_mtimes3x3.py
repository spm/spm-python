from spm.__wrapper__ import Runtime


def _mtimes3x3(*args, **kwargs):
    """
      MTIMES3X3 compute x*y where the dimensionatity is 3x3xN or 3x3xNxM  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/mtimes3x3.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mtimes3x3", *args, **kwargs)
