from spm.__wrapper__ import Runtime


def _nut_sLORETA(*args, **kwargs):
    """
      weight=nut_sLORETA(Lp,data,flags)  
        inputs for regularization contant:  
        [1] data.Ryy = sample covariance, for data-dependent regularization  
        [2] flags.gamma = user defined regularization constant, or 'auto' for  
            leadfield-based regularization  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/nut_sLORETA.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("nut_sLORETA", *args, **kwargs)
