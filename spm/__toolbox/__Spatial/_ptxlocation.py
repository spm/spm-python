from spm.__wrapper__ import Runtime


def _ptxlocation(*args, **kwargs):
  """  Location of a PTX file used in GPU computations  
    FORMAT ptx = ptxlocation(nam)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/private/ptxlocation.m)
  """

  return Runtime.call("ptxlocation", *args, **kwargs)
