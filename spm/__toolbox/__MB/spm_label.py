from spm.__wrap__ import _Runtime


def spm_label(*args, **kwargs):
  """  Factorisation-based Image Labelling  
    FORMAT out = spm_label(cfg)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MB/spm_label.m)
  """

  return _Runtime.call("spm_label", *args, **kwargs)
