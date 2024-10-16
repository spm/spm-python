from spm.__wrapper__ import Runtime


def pullg(*args, **kwargs):
  """  GPU single precision pullg  
    FORMAT g1 = pullg(f0, phi, sett)  
    f0   - 3D float array  
    phi  - 4D float array (dim(4)=3)  
    sett - Settings  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/pullg.m)
  """

  return Runtime.call("pullg", *args, **kwargs)
