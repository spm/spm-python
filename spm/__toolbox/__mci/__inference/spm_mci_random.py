from spm.__wrap__ import _Runtime


def spm_mci_random(*args, **kwargs):
  """  Random effects estimation  
    FORMAT [S] = spm_mci_random (mcmc,R,v,M,U,Y)  
     
    mcmc  Sampling parameters  
    R     Priors on random effects (R.pE, R.pC)  
    v     Fixed effects  
    M     Model Structure (single subject)  
    U     Inputs (single subject)  
    Y     Data (single subject)  
     
    S     Samples, [maxits x M.n]   
     
    Uses Langevin Monte Carlo  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_random.m)
  """

  return _Runtime.call("spm_mci_random", *args, **kwargs)
