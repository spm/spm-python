from spm.__wrapper__ import Runtime


def spm_bilinear_condition(*args, **kwargs):
  """  Condition a bilinear operator by suppressing positive eigenmodes  
    FORMAT M0 = spm_bilinear_condition(M0)  
    M0 - bilinear operator  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_bilinear_condition.m)
  """

  return Runtime.call("spm_bilinear_condition", *args, **kwargs)
