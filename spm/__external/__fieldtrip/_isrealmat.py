from spm._runtime import Runtime


def _isrealmat(*args, **kwargs):
    """
      ISREALMAT returns true for a real matrix  
         
        Use as  
          status = isrealmat(x)  
         
        See also ISNUMERIC, ISREAL, ISVECTOR, ISREALVEC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/isrealmat.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("isrealmat", *args, **kwargs)
