from spm.__wrap__ import _Runtime


def pull(*args, **kwargs):
  """  GPU single precision pull  
    FORMAT f1 = pull(f0, phi, sett)  
    f0   - 3D float array  
    phi  - 4D float array (dim(4)=3)  
    sett - Settings  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/pull.m)
  """

  return _Runtime.call("pull", *args, **kwargs)
