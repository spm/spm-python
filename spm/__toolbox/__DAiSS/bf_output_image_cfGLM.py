from spm.__wrap__ import _Runtime


def bf_output_image_cfGLM(*args, **kwargs):
  """  Compute phase-amplitude coupling using a general linear model  
    currently takes both low frequency phase and amplitude as regressors  
    needs epoched data - uses epochs for statistics  
    writes out images for summary phase-amplitude coupling and  
    amplitude-amplitude coupling, as well as B coefficients per trial  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_image_cfGLM.m)
  """

  return _Runtime.call("bf_output_image_cfGLM", *args, **kwargs)
