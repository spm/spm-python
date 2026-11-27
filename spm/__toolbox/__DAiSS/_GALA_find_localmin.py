from spm._runtime import Runtime


def _GALA_find_localmin(*args, **kwargs):
    r"""
    GALA_find_localmin is a function.  
          regions = GALA_find_localmin(lJcov, Nl, Nd, A, thresh)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/private/GALA_find_localmin.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("GALA_find_localmin", *args, **kwargs)
