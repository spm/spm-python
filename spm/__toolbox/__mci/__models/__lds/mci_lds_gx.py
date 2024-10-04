from spm.__wrap__ import _Runtime


def mci_lds_gx(*args, **kwargs):
  """  Observation function for LDS  
    FORMAT [y,L] = mci_lds_gx (x,u,P,M)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_gx.m)
  """

  return _Runtime.call("mci_lds_gx", *args, **kwargs)
