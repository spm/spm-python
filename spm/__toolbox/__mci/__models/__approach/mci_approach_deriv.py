from mpython import Runtime


def mci_approach_deriv(*args, **kwargs):
    """
      Gradient of log-likelihood for approach model
        FORMAT [dLdp,iCpY,L] = mci_approach_deriv (P,M,U,Y)

        dLdp      gradient of log joint
        iCpY      curvature (Fisher Information)
        L         log joint
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/approach/mci_approach_deriv.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_approach_deriv", *args, **kwargs)
