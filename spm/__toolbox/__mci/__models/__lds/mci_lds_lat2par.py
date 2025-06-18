from mpython import Runtime


def mci_lds_lat2par(*args, **kwargs):
    """
      Convert latent params to params
        FORMAT [Pt,a,b] = mci_lds_lat2par (P,M)

        P         Parameters (latent)
        M         model structure

        Pt        Parameters (transformed)
        a         diagonal values
        b         off-diagonal values
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_lat2par.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_lds_lat2par", *args, **kwargs)
