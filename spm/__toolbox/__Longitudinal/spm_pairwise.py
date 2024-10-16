from spm.__wrapper__ import Runtime


def spm_pairwise(*args, **kwargs):
  """  Longitudinal registration of image pairs  
    FORMAT out = spm_pairwise(job)  
    See tbx_cfg_longitudinal.m for a description of the various fields.   
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Longitudinal/spm_pairwise.m)
  """

  return Runtime.call("spm_pairwise", *args, **kwargs)
