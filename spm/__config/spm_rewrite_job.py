from spm.__wrapper__ import Runtime


def spm_rewrite_job(*args, **kwargs):
  """  Rewrite a batch job for SPM12  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_rewrite_job.m)
  """

  return Runtime.call("spm_rewrite_job", *args, **kwargs)
