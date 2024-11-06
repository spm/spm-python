from spm.__wrapper__ import Runtime


def bf_inverse(*args, **kwargs):
    """
      Compute inverse projectors  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_inverse", *args, **kwargs)
