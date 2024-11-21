from spm.__wrapper__ import Runtime


def spm_mci_popdef(*args, **kwargs):
    """
      Set default parameters for population MCMC  
        FORMAT [mh] = spm_mci_popdef (scale,tune,samp)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_popdef.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_popdef", *args, **kwargs)
