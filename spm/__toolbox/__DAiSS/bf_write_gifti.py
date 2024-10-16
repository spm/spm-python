from spm.__wrapper__ import Runtime


def bf_write_gifti(*args, **kwargs):
  """  Write out beamformer results as GIfTI meshes  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_write_gifti.m)
  """

  return Runtime.call("bf_write_gifti", *args, **kwargs)
