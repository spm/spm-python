from mpython import Runtime


def mci_ramsay_struct(*args, **kwargs):
    """
      Data structures for Ramsay model
        FORMAT [M,U] = mci_ramsay_struct (sigme_e)

        sigma_e       Noise SD

        M,U           model, input data structures
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/ramsay/mci_ramsay_struct.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_ramsay_struct", *args, **kwargs)
