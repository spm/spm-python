from spm.__wrapper__ import Runtime


def spm_mvb_display(*args, **kwargs):
  """  Model display for MVB  
    FORMAT spm_mvb_display(MVB)  
    MVB  - multivariate Bayes structure, select one if not provided  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mvb_display.m)
  """

  return Runtime.call("spm_mvb_display", *args, **kwargs, nargout=0)
