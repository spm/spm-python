from spm.__wrapper__ import Runtime


def bf_isfield(*args, **kwargs):
  """  Efficiently identify if a field is contained within a BF file  
    FORMAT bool = bf_isfield(BF,field)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_isfield.m)
  """

  return Runtime.call("bf_isfield", *args, **kwargs)
