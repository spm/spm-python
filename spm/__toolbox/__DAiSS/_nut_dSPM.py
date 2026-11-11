from spm._runtime import Runtime


def _nut_dSPM(*args, **kwargs):
    r"""
      [weight,eta]=nut_dSPM(Lp,data,flags)  
        Lp : lead field  
        inputs for regularization contant:  
        [1] data.Ryy = sample covariance, for data-dependent regularization  
        [2] flags.gamma = user defined regularization constant, or 'auto' for  
            leadfield-based regularization  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/private/nut_dSPM.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("nut_dSPM", *args, **kwargs)
