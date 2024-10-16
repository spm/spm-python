from spm.__wrapper__ import Runtime


def spm_opt_bfun(*args, **kwargs):
  """   
    FORMAT spm_opt_bfun  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_opt_bfun.m)
  """

  return Runtime.call("spm_opt_bfun", *args, **kwargs, nargout=0)
