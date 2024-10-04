from spm.__wrap__ import _Runtime


def mci_approach_struct(*args, **kwargs):
  """  Approach model structure  
    FORMAT [M,U] = mci_approach_struct (Nobs)  
     
    Nobs      Number of observations  
    M         Model structure  
    U         Input structure  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/approach/mci_approach_struct.m)
  """

  return _Runtime.call("mci_approach_struct", *args, **kwargs)
