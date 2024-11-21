from spm.__wrapper__ import Runtime


def _GALA_find_localmin(*args, **kwargs):
    """
    GALA_find_localmin is a function.  
          regions = GALA_find_localmin(lJcov, Nl, Nd, A, thresh)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/GALA_find_localmin.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("GALA_find_localmin", *args, **kwargs)
