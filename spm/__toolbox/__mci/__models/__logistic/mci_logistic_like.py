from mpython import Runtime


def mci_logistic_like(*args, **kwargs):
    """
      Compute log likelihood of logistic model
        FORMAT [L,E,st] = mci_logistic_like (P,M,U,Y)

        P         parameters
        M         model
        U         inputs
        Y         data

        L         Log likelihood
        E         Errors
        st        Status flag (0 for OK, -1 for problem)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/logistic/mci_logistic_like.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_logistic_like", *args, **kwargs)
