from spm.__wrap__ import _Runtime


def mci_linsqr_gen(*args, **kwargs):
  """  Output of linear model with squared params  
    FORMAT [y] = mci_linsqr_gen (theta,M,U)  
     
    theta     regression coefficients  
    M         model structure  
    U         U.X contains design matrix  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/linsqr/mci_linsqr_gen.m)
  """

  return _Runtime.call("mci_linsqr_gen", *args, **kwargs)
