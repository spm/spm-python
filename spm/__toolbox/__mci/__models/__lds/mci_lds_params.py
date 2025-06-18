from mpython import Runtime


def mci_lds_params(*args, **kwargs):
    """
      LDS constrained: sample params from prior
        FORMAT [P] = mci_lds_params (M,U)

        M     Model structure
        U     Inputs

        P     Parameters
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_params.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_lds_params", *args, **kwargs)
