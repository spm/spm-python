from spm.__wrapper__ import Runtime


def spm_mci_diag(*args, **kwargs):
    """
      Monte Carlo Diagnostics  
        FORMAT [mess] = spm_mci_diag (post,diag)  
         
        post      posterior distribution  
        diag      diagnostic info  
                  .ind            indices of samples to look at  
                  .traceplot      (1/0) for trace plots  
                  .autoplot       (1/0) for autocorrelations  
                  .essplot        (1/0) for effective sample sizes  
                  .eplot          (1/0) for energy (neg log joint) traj  
                  .bplot          (1/0) for Bayes factor of f/b transitions  
         
        ess      effective sample size (for each parameter)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_diag.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_diag", *args, **kwargs)
