from spm.__wrap__ import _Runtime


def spm_mb_output(*args, **kwargs):
  """  Write output from groupwise normalisation and segmentation of images  
    FORMAT res = spm_mb_output(cfg)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_output.m)
  """

  return _Runtime.call("spm_mb_output", *args, **kwargs)
