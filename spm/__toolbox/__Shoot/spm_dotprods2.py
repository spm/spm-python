from spm.__wrap__ import _Runtime


def spm_dotprods2(*args, **kwargs):
  """  Generate a kernel from dot-products of images  
    FORMAT spm_dotprods(job)  
    job.images  - Images to use  
    job.dotprod - Part of filename for results  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_dotprods2.m)
  """

  return _Runtime.call("spm_dotprods2", *args, **kwargs)
