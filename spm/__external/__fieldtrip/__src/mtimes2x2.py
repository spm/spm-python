from spm.__wrapper__ import Runtime


def mtimes2x2(*args, **kwargs):
    """
      MTIMES2X2 compute x*y where the dimensionatity is 2x2xN or 2x2xNxM  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/src/mtimes2x2.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mtimes2x2", *args, **kwargs)
