from spm.__wrap__ import _Runtime


def spm_ov_display(*args, **kwargs):
  """  Display tool - plugin for spm_orthviews  
     
    This routine is a plugin to spm_orthviews. For general help about  
    spm_orthviews and plugins type  
                help spm_orthviews  
    at the MATLAB prompt.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_orthviews/spm_ov_display.m)
  """

  return _Runtime.call("spm_ov_display", *args, **kwargs)
