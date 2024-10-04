from spm.__wrap__ import _Runtime


def mci_approach_like(*args, **kwargs):
  """  Log-likelihood for approach model   
    FORMAT [L,yhat,st] = mci_approach_like (P,M,U,Y)  
     
    P         parameters  
    M,U,Y     as usual  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/approach/mci_approach_like.m)
  """

  return _Runtime.call("mci_approach_like", *args, **kwargs)
