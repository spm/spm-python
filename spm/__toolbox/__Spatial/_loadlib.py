from spm.__wrapper__ import Runtime


def _loadlib(*args, **kwargs):
  """  Load a shared library into MATLAB  
    FORMAT loadlib(nam)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/private/loadlib.m)
  """

  return Runtime.call("loadlib", *args, **kwargs, nargout=0)
