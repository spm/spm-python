from spm.__wrap__ import _Runtime


def spm_mci_mh(*args, **kwargs):
  """  Metropolis Hastings with Gaussian priors and proposals  
    FORMAT [P,L,D] = spm_mci_mh (mcmc,M,U,Y)  
      
    mcmc      Optimisation parameters  eg.  
     
    .nsamp    number of samples to return   
    .Cprop    proposal density  
    .init     initial parameter point  
     
    M         Model structure  
    U         Inputs  
    Y         Data   
     
    P         Posterior samples   
    L         Logjoint history  
    D         Diagnostics (D.accept_rate, D.els)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_mh.m)
  """

  return _Runtime.call("spm_mci_mh", *args, **kwargs)
