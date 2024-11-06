from spm.__wrapper__ import Runtime


def _vbfa_aug2015(*args, **kwargs):
    """
      Output  
        Regularized noise covariance from pre-stimulus data  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/vbfa_aug2015.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("vbfa", *args, **kwargs)
