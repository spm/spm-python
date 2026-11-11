from spm._runtime import Runtime


def spm_mci_minit(*args, **kwargs):
    r"""
      Check and initialise model strucuture  
        FORMAT [M] = spm_mci_minit (M)  
         
        eg. Pre-compute quantities for computing log-joint  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_minit.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_minit", *args, **kwargs)
