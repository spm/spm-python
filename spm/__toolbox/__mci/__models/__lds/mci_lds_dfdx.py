from mpython import Runtime


def mci_lds_dfdx(*args, **kwargs):
    """
      Jacobian for linear system, dx/dt=Ax, with constrained connectivity
        FORMAT [A,Pt] = mci_lds_dfdx (x,u,P,M)

        x     State vector
        u     input
        P     parameters (vectorised)
        M     model structure

        A     f=Ax
        Pt    Parameters (transformed from latent pars)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_dfdx.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_lds_dfdx", *args, **kwargs)
