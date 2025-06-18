from mpython import Runtime


def mci_pb_like(*args, **kwargs):
    """
      Log-likelihood for Preece-Baines model
        FORMAT [L,yhat,st] = mci_pb_like (P,M,U,Y)

        P         parameters
        M,U,Y     as usual
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/growth/mci_pb_like.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_pb_like", *args, **kwargs)
