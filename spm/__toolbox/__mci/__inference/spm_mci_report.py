from spm.__wrap__ import _Runtime


def spm_mci_report(*args, **kwargs):
  """  Report on posterior density from MCI  
    FUNCTION [Ep,SDp] = spm_mci_report (P,mcmc,true_P)  
     
    P         Samples  
    mcmc      Sampling options  
      
    Ep        Posterior mean  
    SDp       Posterior SD  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_report.m)
  """

  return _Runtime.call("spm_mci_report", *args, **kwargs)
