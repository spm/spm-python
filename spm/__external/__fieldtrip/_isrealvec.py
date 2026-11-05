from spm._runtime import Runtime


def _isrealvec(*args, **kwargs):
    r"""
      ISREALVEC returns true for a real row or column vector  
         
        Use as  
          status = isrealvec(x)  
         
        See also ISNUMERIC, ISREAL, ISVECTOR, ISREALMAT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/isrealvec.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("isrealvec", *args, **kwargs)
