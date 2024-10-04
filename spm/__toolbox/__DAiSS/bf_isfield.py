from spm.__wrap__ import _Runtime


def bf_isfield(*args, **kwargs):
  """  Efficiently identify if a field is contained within a BF file  
    FORMAT bool = bf_isfield(BF,field)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_isfield.m)
  """

  return _Runtime.call("bf_isfield", *args, **kwargs)
