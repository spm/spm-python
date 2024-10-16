from spm.__wrapper__ import Runtime


def mci_linear_gen(*args, **kwargs):
  """  Output of linear model  
    FORMAT [y] = mci_linear_gen (theta,M,U)  
     
    theta     regression coefficients  
    M         model structure  
    U         U.X contains design matrix  
     
    y         outputs  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/linear/mci_linear_gen.m)
  """

  return Runtime.call("mci_linear_gen", *args, **kwargs)
