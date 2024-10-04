from spm.__wrap__ import _Runtime


def mci_pb_like(*args, **kwargs):
  """  Log-likelihood for Preece-Baines model   
    FORMAT [L,yhat,st] = mci_pb_like (P,M,U,Y)  
     
    P         parameters  
    M,U,Y     as usual  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/growth/mci_pb_like.m)
  """

  return _Runtime.call("mci_pb_like", *args, **kwargs)
