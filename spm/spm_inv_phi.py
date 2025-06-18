from mpython import Runtime


def spm_inv_phi(*args, **kwargs):
    """
      Inverse logistic function
        FORMAT [y] = spm_inv_phi(x)

        x   = log((y./(1 - y))
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_inv_phi.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_inv_phi", *args, **kwargs)
