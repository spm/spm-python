from mpython import Runtime


def mci_linear_post(*args, **kwargs):
    """
      Analytic posterior for linear regression
        FORMAT [Ep,Cp,L] = mci_linear_post (M,U,Y)

        M     Model Structure
        U     Inputs
        Y     Data

        Ep    Posterior mean
        Cp    Posterior covariance
        L     Log evidence
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/linear/mci_linear_post.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_linear_post", *args, **kwargs)
