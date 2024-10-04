from spm.__wrap__ import _Runtime


def lbessi(*args, **kwargs):
  """  GPU single precision f = log(besseli(nu, z))  
    FORMAT f = lbessi(nu,z)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/lbessi.m)
  """

  return _Runtime.call("lbessi", *args, **kwargs)
