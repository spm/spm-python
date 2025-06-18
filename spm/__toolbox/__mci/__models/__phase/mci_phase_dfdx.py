from mpython import Runtime


def mci_phase_dfdx(*args, **kwargs):
    """
      State sensitivity for phase model
        FORMAT [dfdx] = mci_phase_dfdx (x,u,P,M)

        x      state vector
        M      model structure
        P      parameter vector

        dfdx   Jacobian wrt states
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_phase_dfdx.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_phase_dfdx", *args, **kwargs)
