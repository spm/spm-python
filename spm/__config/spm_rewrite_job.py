from spm.__wrap__ import _Runtime


def spm_rewrite_job(*args, **kwargs):
  """  Rewrite a batch job for SPM12  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_rewrite_job.m)
  """

  return _Runtime.call("spm_rewrite_job", *args, **kwargs)
