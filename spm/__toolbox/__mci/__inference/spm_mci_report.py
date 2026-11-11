from spm._runtime import Runtime


def spm_mci_report(*args, **kwargs):
    r"""
      Report on posterior density from MCI  
        FUNCTION [Ep,SDp] = spm_mci_report (P,mcmc,true_P)  
         
        P         Samples  
        mcmc      Sampling options  
          
        Ep        Posterior mean  
        SDp       Posterior SD  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_report.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_report", *args, **kwargs)
