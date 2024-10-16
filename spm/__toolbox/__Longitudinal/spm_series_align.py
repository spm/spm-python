from spm.__wrapper__ import Runtime


def spm_series_align(*args, **kwargs):
  """  Longitudinal registration of image series  
    FORMAT out = spm_series_align(job)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Longitudinal/spm_series_align.m)
  """

  return Runtime.call("spm_series_align", *args, **kwargs)
