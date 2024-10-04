from spm.__wrap__ import _Runtime


def spm_sextract(*args, **kwargs):
  """  Surface extraction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/SRender/spm_sextract.m)
  """

  return _Runtime.call("spm_sextract", *args, **kwargs)
