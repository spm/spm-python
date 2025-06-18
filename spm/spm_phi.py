from mpython import Runtime


def spm_phi(*args, **kwargs):
    """
      Logistic function
        FORMAT [y] = spm_phi(x)

        y   = 1./(1 + exp(-x))
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_phi.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_phi", *args, **kwargs)
