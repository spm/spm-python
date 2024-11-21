from spm.__wrapper__ import Runtime


def _GALA_invert(*args, **kwargs):
    """
    GALA_invert is a function.  
          [J, S] = GALA_invert(BF, tS)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/GALA_invert.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("GALA_invert", *args, **kwargs)
