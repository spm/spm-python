from mpython import Runtime


def _nut_dSPM(*args, **kwargs):
    """
      [weight,eta]=nut_dSPM(Lp,data,flags)
        Lp : lead field
        inputs for regularization contant:
        [1] data.Ryy = sample covariance, for data-dependent regularization
        [2] flags.gamma = user defined regularization constant, or 'auto' for
            leadfield-based regularization


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/nut_dSPM.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("nut_dSPM", *args, **kwargs)
