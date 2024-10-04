from spm.__wrap__ import _Runtime


def spm_mci_isvl(*args, **kwargs):
  """  Compute Log Evidence using Importance Sampling   
    FORMAT [isvl] = spm_mci_isvl (mcmc,M,U,Y,VL)  
     
    mcmc          Optimisation parameters  eg.  
     
    .maxits       number of samples to use  
     
    M             Model structure   
    U             Input structure  
    Y             Data   
     
    isvl            
    .logev         log evidence  
    .L(s)          log likelihood of sth sample  
    .v(s)          importance weight of sth sample  
    .logev_est(S)  estimate based on first S samples only  
    .logev_boot(b) estimate based on bth bootstrap resample (of size .maxits)  
     
    Uses IS with VL posterior as proposal  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_isvl.m)
  """

  return _Runtime.call("spm_mci_isvl", *args, **kwargs)
