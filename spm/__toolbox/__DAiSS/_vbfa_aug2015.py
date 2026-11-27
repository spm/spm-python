from spm._runtime import Runtime


def _vbfa_aug2015(*args, **kwargs):
    r"""
      Output  
        Regularized noise covariance from pre-stimulus data  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/private/vbfa_aug2015.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("vbfa", *args, **kwargs)
