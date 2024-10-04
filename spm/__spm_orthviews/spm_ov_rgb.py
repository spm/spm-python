from spm.__wrap__ import _Runtime


def spm_ov_rgb(*args, **kwargs):
  """  RGB overlays - plugin for spm_orthviews  
    A shorthand to overlaying the absolute value of three different images  
    onto a displayed image in colours red, green and blue. The overlay images  
    are optionally masked and multiplied with a scaling image. The displayed  
    overlay images are the absolute value of the given overlays.  
     
    This routine is a plugin to spm_orthviews. For general help about  
    spm_orthviews and plugins type  
                help spm_orthviews  
    at the MATLAB prompt.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_orthviews/spm_ov_rgb.m)
  """

  return _Runtime.call("spm_ov_rgb", *args, **kwargs)
