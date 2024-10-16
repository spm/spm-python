from spm.__wrapper__ import Runtime


def mci_linsqr_gen(*args, **kwargs):
  """  Output of linear model with squared params  
    FORMAT [y] = mci_linsqr_gen (theta,M,U)  
     
    theta     regression coefficients  
    M         model structure  
    U         U.X contains design matrix  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/linsqr/mci_linsqr_gen.m)
  """

  return Runtime.call("mci_linsqr_gen", *args, **kwargs)
