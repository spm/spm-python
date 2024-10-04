from spm.__wrap__ import _Runtime


def mci_discount_like(*args, **kwargs):
  """  Compute log likelihood of discount model  
    FORMAT [L,E,st] = mci_discount_like (P,M,U,Y)  
     
    P         parameters  
    M         model  
    U         inputs  
    Y         data  
      
    L         Log likelihood  
    E         Errors  
    st        Status flag (0 for OK, -1 for problem)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/discount/mci_discount_like.m)
  """

  return _Runtime.call("mci_discount_like", *args, **kwargs)
