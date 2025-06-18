from mpython import Runtime


def spm_mci_switch_prep(*args, **kwargs):
    """
      Prepare quantities for computing log prior in SVD-reduced space
        FORMAT [M] = spm_mci_switch_prep (M)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_switch_prep.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_switch_prep", *args, **kwargs)
