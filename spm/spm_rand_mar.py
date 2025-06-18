from mpython import Runtime


def spm_rand_mar(*args, **kwargs):
    """
      Generate random variates from an autoregressive process
        FORMAT [y] = spm_rand_mar(m,n,a)
        m   - time bins
        n   - variates
        a   - autoregression coefficients

        see also: spm_rand_power_law
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_rand_mar.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_rand_mar", *args, **kwargs)
