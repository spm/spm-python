from spm.__wrapper__ import Runtime


def spm_mci_post(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_post.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_post", *args, **kwargs)
