from spm.__wrapper__ import Runtime


def spm_lincom(*args, **kwargs):
  """  Generate linear combinations of images  
    FORMAT spm_lincom(job)  
    job.images   - Images to use  
    job.weights  - Matrix of weights  
    job.basename - Part of filename for results  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_lincom.m)
  """

  return Runtime.call("spm_lincom", *args, **kwargs)
