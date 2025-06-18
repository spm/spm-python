from mpython import Runtime


def mci_discount_struct(*args, **kwargs):
    """
      Set up data structures for discounting model
        FORMAT [M,U] = mci_discount_struct (Nobs)

        Nobs      number of data points

        M         model structure
        U         U.X is the design matrix
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/discount/mci_discount_struct.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_discount_struct", *args, **kwargs)
