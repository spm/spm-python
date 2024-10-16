from spm.__wrapper__ import Runtime


def mci_discount_struct(*args, **kwargs):
  """  Set up data structures for discounting model  
    FORMAT [M,U] = mci_discount_struct (Nobs)  
     
    Nobs      number of data points  
     
    M         model structure  
    U         U.X is the design matrix  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/discount/mci_discount_struct.m)
  """

  return Runtime.call("mci_discount_struct", *args, **kwargs)
