from spm.__wrapper__ import Runtime


def _isrealvec(*args, **kwargs):
    """
      ISREALVEC returns true for a real row or column vector  
         
        Use as  
          status = isrealvec(x)  
         
        See also ISNUMERIC, ISREAL, ISVECTOR, ISREALMAT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/isrealvec.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("isrealvec", *args, **kwargs)
