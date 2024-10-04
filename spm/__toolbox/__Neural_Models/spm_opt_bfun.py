from spm.__wrap__ import _Runtime


def spm_opt_bfun(*args, **kwargs):
  """   
    FORMAT spm_opt_bfun  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_opt_bfun.m)
  """

  return _Runtime.call("spm_opt_bfun", *args, **kwargs, nargout=0)
