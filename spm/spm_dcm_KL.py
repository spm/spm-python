from spm.__wrapper__ import Runtime


def spm_dcm_KL(*args, **kwargs):
  """  Compute the distance between two models based on prior responses  
    FORMAT [D,C,K] = spm_dcm_KL(Mi,Mj)  
     
    M{1:n}   - structure array of models  
     
    D(n x n) - distance matrix (KL divergence)  
    C{1:n}   - response covariances  
    K{1:n}   - response means  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dcm_KL.m)
  """

  return Runtime.call("spm_dcm_KL", *args, **kwargs)
