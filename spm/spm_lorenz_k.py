from mpython import Runtime


def spm_lorenz_k(*args, **kwargs):
    """
      Equations of motion for coupled Lorenz attractors
        FORMAT [f] = spm_lorenz_k(x,v,P)
        x - hidden states (3 x N)
        v - exogenous input
        P - parameters
            P.t = N x 1
            P.k = 1 x 1
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_lorenz_k.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_lorenz_k", *args, **kwargs)
