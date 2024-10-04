from spm.__wrap__ import _Runtime


def spm_find_pC(*args, **kwargs):
  """  Utility routine that finds the indices of non-zero covariance  
    FORMAT [i,pC,pE,Np] = spm_find_pC(pC,pE,fields)  
    FORMAT [i,pC,pE,Np] = spm_find_pC(DCM,fields)  
    FORMAT [i,pC,pE,Np] = spm_find_pC(DCM)  
      
    pC     - covariance matrix or variance structure  
    pE     - parameter structure  
    fields - desired fields of pE  
     
    or  
     
    DCM    - DCM structure  
     
    i      - find(diag(pC) > TOL)  
    rC     - reduced covariances  
    rE     - reduced expectation  
      
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_find_pC.m)
  """

  return _Runtime.call("spm_find_pC", *args, **kwargs)
