from spm.__wrap__ import _Runtime


def spm_markdown(*args, **kwargs):
  """  Convert a job configuration tree into a series of markdown documents  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_markdown.m)
  """

  return _Runtime.call("spm_markdown", *args, **kwargs, nargout=0)
