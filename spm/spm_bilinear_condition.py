from spm.__wrap__ import _Runtime


def spm_bilinear_condition(*args, **kwargs):
  """  Condition a bilinear operator by suppressing positive eigenmodes  
    FORMAT M0 = spm_bilinear_condition(M0)  
    M0 - bilinear operator  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_bilinear_condition.m)
  """

  return _Runtime.call("spm_bilinear_condition", *args, **kwargs)
