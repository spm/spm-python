from spm.__wrap__ import _Runtime


def spm_mvb_cvk_display(*args, **kwargs):
  """  Model display for MVB with cross-validation  
    FORMAT spm_mvb_cvk_display(MVB)  
    MVB  - multivariate Bayes structure, select one if not provided  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mvb_cvk_display.m)
  """

  return _Runtime.call("spm_mvb_cvk_display", *args, **kwargs, nargout=0)
