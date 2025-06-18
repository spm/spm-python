from mpython import Runtime


def spm_ness_flows(*args, **kwargs):
    """
      Nonequilibrium steady-state under a Helmholtz decomposition
        FORMAT spm_ness_flows(M,x)
       --------------------------------------------------------------------------
        M   - model specification structure
        Required fields:
           M.X  - sample points
           M.W  - (n x n) - precision matrix of random fluctuations
           M.K  - order of polynomial expansion
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ness_flows.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ness_flows", *args, **kwargs, nargout=0)
