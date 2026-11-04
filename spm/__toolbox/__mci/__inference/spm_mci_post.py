from spm._runtime import Runtime


def spm_mci_post(*args, **kwargs):
    r"""
      Estimate posterior density  
        FORMAT [post] = spm_mci_post (mcmc,M,U,Y,true_P)  
         
        mcmc          .inference = 'amc','ais','vl' or 'langevin'   
                      .verbose = 0 or 1 to plot progress (default 0)  
                      .maxits = max number of iterations for sampling  
                      .init = init parameter values (default is prior mean)  
        M             model structure  
        U             inputs (shouldn't be empty)  
        Y             data  
        true_P        true parameters (if known)  
         
        post          structure containing posterior (mean, samples etc)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_post.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_post", *args, **kwargs)
