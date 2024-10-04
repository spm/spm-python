from spm.__wrap__ import _Runtime


def spm_ADEM_update(*args, **kwargs):
  """  Update ADEM structure using conditional expectations  
    FORMAT DEM = spm_ADEM_update(DEM,COV)  
     
    DEM - DEM structure  
    COV - Covariance of parameter (P) fluctuations (E): P(i + 1) = P(i) + E  
        - where cov(E) = COV*pC  
     
    This routine updates posterior expectations about states and parameters  
    by replacing prior expectations with posterior expectations (and  
    similarly updating hidden states and causes to the final iteration). If  
    called with an extra argument, the posterior variances of the  
    parameters are also updated.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_ADEM_update.m)
  """

  return _Runtime.call("spm_ADEM_update", *args, **kwargs)
