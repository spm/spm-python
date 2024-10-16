from spm.__wrapper__ import Runtime


def lbessi(*args, **kwargs):
  """  GPU single precision f = log(besseli(nu, z))  
    FORMAT f = lbessi(nu,z)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/lbessi.m)
  """

  return Runtime.call("lbessi", *args, **kwargs)
