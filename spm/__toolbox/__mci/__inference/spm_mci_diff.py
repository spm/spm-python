from mpython import Runtime


def spm_mci_diff(*args, **kwargs):
    """
      Compute gradient and curvature of log likelihood using finite differences
        FORMAT [dLdp,iCpY,L] = spm_mci_diff (P,M,U,Y)

        dLdp      gradient of log likelihood
        iCpY      curvature (observed Fisher Information)
        L         log likelihood
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_diff.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_diff", *args, **kwargs)
