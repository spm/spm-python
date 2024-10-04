from spm.__wrap__ import _Runtime


def mci_discount_act(*args, **kwargs):
  """  Activation of discounting model  
    FORMAT [a,v1,v2,k] = mci_discount_act (P,M,U)  
     
    P         parameters  
    M         model structure  
    U         contains rewards and times  
     
    a         activation for discount model  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/discount/mci_discount_act.m)
  """

  return _Runtime.call("mci_discount_act", *args, **kwargs)
