from spm.__wrap__ import _Runtime


def spm_mci_glike(*args, **kwargs):
  """  Gaussian Log-likelihood   
    FORMAT [L,e,st] = spm_mci_glike (P,M,U,Y,G)  
     
    P         Parameters  
    M         Model structure  
    U         Inputs  
    Y         Data  
    G         Predictions (computed if not provided)  
      
    L         Log Likelihood  
    e         Errors  
    st        Status flag (0 for OK, -1 for problem)  
     
    Assumes diagonal error covariance M.Ce  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_glike.m)
  """

  return _Runtime.call("spm_mci_glike", *args, **kwargs)
