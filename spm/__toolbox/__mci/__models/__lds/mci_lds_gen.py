from mpython import Runtime


def mci_lds_gen(*args, **kwargs):
    """
      LDS constrained: generate data
        FORMAT [Y] = mci_lds_gen (M,U,P)

        M     Model structure
        U     Inputs
        P     Parameters

        Y     Data
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_gen.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_lds_gen", *args, **kwargs)
