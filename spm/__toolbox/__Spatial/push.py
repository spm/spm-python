from spm.__wrap__ import _Runtime


def push(*args, **kwargs):
  """  GPU single precision push  
    FORMAT f0 = push(f1, phi, dm0, sett)  
    f1   - 3D float array  
    phi  - 4D float array (dim(4)=3)  
    dm0  - Output dimensions  
    sett - Settings  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/push.m)
  """

  return _Runtime.call("push", *args, **kwargs)
