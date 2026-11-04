from spm._runtime import Runtime


def _isrealmat(*args, **kwargs):
    r"""
      ISREALMAT returns true for a real matrix  
         
        Use as  
          status = isrealmat(x)  
         
        See also ISNUMERIC, ISREAL, ISVECTOR, ISREALVEC  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/isrealmat.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("isrealmat", *args, **kwargs)
