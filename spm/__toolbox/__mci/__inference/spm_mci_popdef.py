from spm._runtime import Runtime


def spm_mci_popdef(*args, **kwargs):
    r"""
      Set default parameters for population MCMC  
        FORMAT [mh] = spm_mci_popdef (scale,tune,samp)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_popdef.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_popdef", *args, **kwargs)
