from mpython import Runtime


def mci_discount_act(*args, **kwargs):
    """
      Activation of discounting model
        FORMAT [a,v1,v2,k] = mci_discount_act (P,M,U)

        P         parameters
        M         model structure
        U         contains rewards and times

        a         activation for discount model
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/discount/mci_discount_act.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_discount_act", *args, **kwargs)
