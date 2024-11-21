from spm.__wrapper__ import Runtime


def spm_dcm_fit(*args, **kwargs):
    """
      Bayesian inversion of DCMs using Variational Laplace  
        FORMAT [DCM] = spm_dcm_fit(P)  
         
        P          - {N x M} DCM structure array (or filenames) from N subjects  
        use_parfor - if true, will attempt to run in parallel (default: false)  
                     NB: all DCMs are loaded into memory  
         
        DCM  - Inverted (1st level) DCM structures with posterior densities  
       __________________________________________________________________________  
         
        This routine is just a wrapper that calls the appropriate dcm inversion  
        routine for a set a pre-specifed DCMs.  
         
        If called with a cell array, each column is assumed to contain 1st level  
        DCMs inverted under the same model. Each row contains a different data  
        set (or subject).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_fit.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fit", *args, **kwargs)
