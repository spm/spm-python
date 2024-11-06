from spm.__wrapper__ import Runtime


def spm_mci_report(*args, **kwargs):
    """
      Report on posterior density from MCI  
        FUNCTION [Ep,SDp] = spm_mci_report (P,mcmc,true_P)  
         
        P         Samples  
        mcmc      Sampling options  
          
        Ep        Posterior mean  
        SDp       Posterior SD  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_report.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_report", *args, **kwargs)
