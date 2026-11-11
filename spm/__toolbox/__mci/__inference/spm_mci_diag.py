from spm._runtime import Runtime


def spm_mci_diag(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_diag.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_diag", *args, **kwargs)
