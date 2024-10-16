from spm.__wrapper__ import Runtime


def spm_mb_output(*args, **kwargs):
  """  Write output from groupwise normalisation and segmentation of images  
    FORMAT res = spm_mb_output(cfg)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_output.m)
  """

  return Runtime.call("spm_mb_output", *args, **kwargs)
