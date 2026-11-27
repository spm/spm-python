from spm._runtime import Runtime


def _GALA_invert(*args, **kwargs):
    r"""
    GALA_invert is a function.  
          [J, S] = GALA_invert(BF, tS)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/private/GALA_invert.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("GALA_invert", *args, **kwargs)
