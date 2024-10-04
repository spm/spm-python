from spm.__wrap__ import _Runtime


def spm_mean_ui(*args, **kwargs):
  """  Prompt for a series of images and averages them  
   __________________________________________________________________________  
     
    This function is deprecated. Use spm_mean instead.  
   __________________________________________________________________________  
    Copyright (C) 1998-2011 Wellcome Trust Centre for Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/compat/spm_mean_ui.m)
  """

  return _Runtime.call("spm_mean_ui", *args, **kwargs, nargout=0)
