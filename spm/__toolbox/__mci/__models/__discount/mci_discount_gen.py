from spm.__wrap__ import _Runtime


def mci_discount_gen(*args, **kwargs):
  """  Output of discounting model  
    FORMAT [g,y] = mci_discount_gen (P,M,U)  
     
    P         parameters  
    M         model structure  
    U         U.X contains design matrix  
     
    g         probability of taking option 1  
    y         binary decisions based on g  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/discount/mci_discount_gen.m)
  """

  return _Runtime.call("mci_discount_gen", *args, **kwargs)
