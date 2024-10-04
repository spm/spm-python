from spm.__wrap__ import _Runtime


def spm_dartel_warp(*args, **kwargs):
  """  Register images to template data  
    format spm_dartel_warp(job)  
     
    The outputs are flow fields.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_dartel_warp.m)
  """

  return _Runtime.call("spm_dartel_warp", *args, **kwargs)
