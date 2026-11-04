from spm._runtime import Runtime


def spm_mci_quantiles(*args, **kwargs):
    r"""
      Plot histogram and quantiles of posterior density  
        FORMAT [y] = spm_mci_quantiles (post,j,q3,expP)  
         
        post      posterior data structure  
        j         jth variate  
        q3        plot quantiles on histogram  
        expP      exponentiate parameters before plotting ?  
         
        y         2.5%, 50%, 97.5% quantiles  
         
        Solid lines show quantiles from posterior samples  
        Dotted lines under Gaussian assumptions  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_quantiles.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_quantiles", *args, **kwargs)
