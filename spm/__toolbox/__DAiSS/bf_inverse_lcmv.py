from spm._runtime import Runtime


def bf_inverse_lcmv(*args, **kwargs):
    """
      Computes LCMV filters  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_lcmv.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_inverse_lcmv", *args, **kwargs)
