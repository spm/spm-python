from mpython import Runtime


def spm_fx_lz(*args, **kwargs):
    """
      flow for Lorenz attractor
        FORMAT [y] = spm_fx_lz(x,u,P)
        x - state
        u - input
        P - parameters
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_fx_lz.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fx_lz", *args, **kwargs)
