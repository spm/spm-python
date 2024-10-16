from spm.__wrapper__ import Runtime


def spm_sextract(*args, **kwargs):
  """  Surface extraction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/SRender/spm_sextract.m)
  """

  return Runtime.call("spm_sextract", *args, **kwargs)
