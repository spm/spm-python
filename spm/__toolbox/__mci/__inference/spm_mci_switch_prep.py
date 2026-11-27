from spm._runtime import Runtime


def spm_mci_switch_prep(*args, **kwargs):
    r"""
      Prepare quantities for computing log prior in SVD-reduced space  
        FORMAT [M] = spm_mci_switch_prep (M)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_switch_prep.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_switch_prep", *args, **kwargs)
