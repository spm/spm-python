from spm._runtime import Runtime


def spm_mci_minit(*args, **kwargs):
    """
      Check and initialise model strucuture  
        FORMAT [M] = spm_mci_minit (M)  
         
        eg. Pre-compute quantities for computing log-joint  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_minit.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_minit", *args, **kwargs)
